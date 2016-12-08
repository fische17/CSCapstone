"""AuthenticationApp Views

Created by Naman Patwari on 10/4/2016.
"""

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages

import logging
logger = logging.getLogger('AuthenticationApp')


from .forms import LoginForm, RegisterForm, UpdateForm, TeacherUpdateForm, EngineerUpdateForm, StudentUpdateForm
from .models import MyUser, Student, Teacher, Engineer

# Auth Views

def auth_login(request):
	form = LoginForm(request.POST or None)
	next_url = request.GET.get('next')
	if next_url is None:
		next_url = "/"
	if form.is_valid():
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		user = authenticate(email=email, password=password)
		if user is not None:
			messages.success(request, 'Success! Welcome, '+(user.first_name or ""))
			login(request, user)
			return HttpResponseRedirect(next_url)
		else:
			messages.warning(request, 'Invalid username or password.')
			
	context = {
		"form": form,
		"page_name" : "Login",
		"button_value" : "Login",
		"links" : ["register"],
	}
	return render(request, 'auth_form.html', context)

def auth_logout(request):
	logout(request)
	messages.success(request, 'Success, you are now logged out')
	return render(request, 'index.html')

def auth_register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/")
	
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		new_user = MyUser.objects.create_user(email=form.cleaned_data['email'], 
			password=form.cleaned_data["password2"]) 
		new_user.first_name=form.cleaned_data['firstname']
		new_user.last_name=form.cleaned_data['lastname']
		new_user.save()	
		#Also registering students		
		if(form.cleaned_data['role'] == "student"):
			new_student = Student(user = new_user)
			new_student.university = form.cleaned_data['university']			
			new_user.is_student = True
			new_student.save()

		#Register Teachers
		if(form.cleaned_data['role']  == "teacher"):
			new_teacher = Teacher(user = new_user)
			new_teacher.university = form.cleaned_data['university']
			new_user.is_teacher = True
			logger.error('hellos')
			new_teacher.save()

		#Register Engineers
		if(form.cleaned_data['role']  == "engineer"):
			new_engineer = Engineer(user = new_user)
			new_user.is_engineer = True
			new_engineer.save()

		new_user.save()

		login(request, new_user);	
		messages.success(request, 'Success! Your account was created.')
		return render(request, 'index.html')

	context = {
		"form": form,
		"page_name" : "Register",
		"button_value" : "Register",
		"links" : ["login"],
	}
	return render(request, 'auth_form.html', context)

@login_required
def update_profile(request):
	form = UpdateForm(request.POST or None, instance=request.user)
	if form.is_valid():
		form.save()
		messages.success(request, 'Success, your profile was saved!')

	context = {
		"form": form,
		"page_name" : "Update",
		"button_value" : "Update",
		"links" : ["logout"],
	}
	return render(request, 'auth_form.html', context)

@login_required
def update_info(request):
	if(request.user.is_teacher):
		form = TeacherUpdateForm(request.POST or None, instance=request.user.teacher)
	elif(request.user.is_engineer):
		form = EngineerUpdateForm(request.POST or None, instance=request.user.engineer)
	else:
		form = StudentUpdateForm(request.POST or None, instance=request.user.student)				
	if form.is_valid():
		form.save()
		messages.success(request, 'Success, your info was save!')
	
	context = {
		"form": form,
		"page_name" : "Update",
		"button_value" : "Update",
		"links" : ["logout"],
	}
	return render(request, 'auth_form.html', context)