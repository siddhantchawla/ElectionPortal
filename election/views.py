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
	return render(request,'home.html',{'user':request.user})



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
@user_passes_test(check_student)
def fillNomination(request):
	applied = Candidate.objects.filter(user_id = request.user.id)
	for application in applied:
		sess = Election.objects.filter(session_id = application.session.session_id)
		sess = sess.first()
		if sess.status == 1:
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
