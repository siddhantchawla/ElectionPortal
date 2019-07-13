from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate, login
import datetime
from .models import *
from .forms import SessionStartForm
# Create your views here.

def check_admin(user):
	return user.is_superuser

def check_student(user):
	return user.is_superuser==0


@login_required(login_url='login/')
@user_passes_test(check_admin)
def index(request):
	fac = request.user
	session_detail = Election.objects.filter(faculty = fac)
	data = {'faculty' : fac}
	data['sessions'] = []
	for sess in session_detail:
		r = {}
		# r['faculty']
		r['post'] = sess.post
		r['year'] = sess.year
		r['session_id'] = sess.session_id
		r['status'] = sess.status
		data['sessions'].append(r)
	return render(request,'home.html',data)



@login_required(login_url='login/')
@user_passes_test(check_admin)
def startSession(request):
	if request.method == 'POST':
		form = SessionStartForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			year = datetime.datetime.now().year
			post = userObj['post']
			# print(year)
			# print(post)
			profile = Election(faculty = request.user)
			profile.year = year
			profile.post = post
			profile.status = 1
			profile.save()
			return redirect('/election/')
		else:
			raise forms.ValidationError('invalid form')
	else:
		form = SessionStartForm()
	return render(request,'sessionStart.html', {'form':form})


@login_required(login_url='login/')
@user_passes_test(check_admin)
def changeStatus(request, session_id):
	session_id = int(session_id)
	obj = Election.objects.filter(session_id = session_id)
	object_detail = obj.first()
	print(object_detail.status)
	if(object_detail.status == 1):
		object_detail.status = 2
		object_detail.save()
	elif(object_detail.status == 2):
		object_detail.status = 3
		object_detail.save()
	# else:
	# 	return redirect('/election/')
	return redirect('/election/')


@login_required(login_url='login/')
@user_passes_test(check_student)
def fillNomination(request):
	applied = Candidate.objects.filter(user_id = request.user.id)
	for application in applied:
		sess = Election.objects.filter(session_id = application.session.session_id)
		sess = sess.first()
		if sess.status != 3:
			return render(request,'fillNomination.html',{})
	sessions = Election.objects.filter(status = 1)
	return render(request,'fillNomination.html',{'sessions':sessions})


@login_required(login_url='login/')
@user_passes_test(check_student)
def apply(request,sessionid):
	sessionid = int(sessionid)
	sess = Election.objects.filter(session_id=sessionid)
	sess = sess.first()
	candidate = Candidate(user_id = request.user.id)
	candidate.session = sess
	candidate.save()
	return redirect('/election/applied')


@login_required(login_url='login/')
@user_passes_test(check_student)
def applied(request):
	applications = []
	sessions = Candidate.objects.filter(user_id = request.user.id)
	for sess in sessions:
		obj = Election.objects.filter(session_id = sess.session.session_id)
		obj = obj.first()
		applications.append(obj)
	return render(request,'applied.html',{'applications':applications})


@login_required(login_url='login/')
@user_passes_test(check_student)
def activeSessions(request):
	sessions = Election.objects.filter(status = 2)
	available = []
	for sess in sessions:
		voted = Voted.objects.filter(session_id = sess.session_id,voter = request.user)
		if not voted:
			available.append(sess)
	return render(request,'activeSessions.html',{'sessions':available})


@login_required(login_url='login/')
@user_passes_test(check_student)
def vote(request,session_id):
	sessionid = int(session_id)
	session = Election.objects.filter(session_id = sessionid)
	session = session.first()
	candidates = Candidate.objects.filter(session = session)
	data = {}
	data['session_id'] = sessionid
	data['post'] = session.post
	data['applicants'] = []
	for candidate in candidates:
		userid = candidate.user_id
		user = User.objects.filter(id = userid)
		user = user.first()
		r = {}
		r['first_name'] = user.first_name
		r['last_name'] = user.last_name
		r['userid'] = userid
		data['applicants'].append(r)

	return render(request,'vote.html',data)

@login_required(login_url='login/')
@user_passes_test(check_student)
def addVote(request,session_id,userid):
	voter = Voted(voter = request.user,session_id = session_id)
	voter.save()
	elec = Election.objects.filter(session_id = session_id)
	elec = elec.first()
	vote = Votecount(session = elec,candidate_id = userid)
	reference_no = vote.reference_no
	vote.save()
	return redirect('/election/activeSessions')


@login_required(login_url='login/')
@user_passes_test(check_admin)
def result(request,session_id):
	sessionid = session_id
	elec = Election.objects.filter(session_id = sessionid)
	elec = elec.first()
	candidates = Candidate.objects.filter(session = elec)
	maxx = 0
	data = {}
	data['result'] = []
	data['winner'] = 0
	for candidate in candidates:
		votes = Votecount.objects.filter(session = elec,candidate_id = candidate.user_id)
		r = {}
		c = len(votes)
		user = User.objects.filter(id = candidate.user_id)
		user = user.first()
		r['votes'] = c
		r['first_name'] = user.first_name
		r['last_name'] = user.last_name
		r['user_id'] = candidate.user_id
		if c > maxx:
			maxx = c
			data['winner'] = candidate.user_id
		data['result'].append(r)
	winner = User.objects.filter(id =data['winner'])
	winner = winner.first()
	result = Result(user = winner,session_id = sessionid)
	return render(request,'result.html',data)


