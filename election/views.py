from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate, login
from .models import *
from .forms import SessionStartForm
# Create your views here.
def startSession(request):
	if request.method == 'POST':
		form = SessionStartForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			year = userObj['year']
			post = userObj['post']
			print(year)
			print(post)
			# fac = Faculty.objects.create(faculty = request.user)
			# fac.save()
			profile = Election.objects.create(faculty = request.user)
			profile.year = year
			profile.post = post
			profile.status = 1
			profile.save()
			return render(request,'home2.html',{user:user})
		else:
			raise forms.ValidationError('invalid form')
	else:
		form = SessionStartForm()
	return render(request,'election/sessionStart.html', {'form':form})