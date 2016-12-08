"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render

from . import models
from . import forms
from datetime import datetime

def getProjects(request):
	projects_list = models.Project.objects.all()
	return render(request, 'projects.html', {
        'projects': projects_list,
    })

def getProject(request):
	in_name = request.GET.get('name', 'None')
	project = models.Project.objects.get(name__exact=in_name)
	return render(request, 'project.html', {
		'projects' : project,
	})
def bookmarkProject(request):



	in_name = request.GET.get('name', 'None')
	project = models.Project.objects.get(name__exact=in_name)
	return render(request, 'successBookmark.html', {
		'project' : project,
	})


	
def getBookmarks(request):
	projects_list = models.Project.objects.all()
	return render(request, 'projects.html', {
        'projects': projects_list,
    })

def getSuggestedProjects(request):
	if request.user.is_authenticated():
		if request.user.is_student:
			projects_list = models.Project.objects.all(programmingLang__icontains=user.language)

			return render(request, 'projects.html', {
				'projects': projects_list,
			})
	return render(request, 'autherror.html')
	

def getProjectFormSuccess(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = forms.ProjectForm(request.POST)
			if form.is_valid():
				in_projectName = form.cleaned_data['name']
				if models.Project.objects.filter(name__exact=in_projectName).exists():
					return render(request, 'addMemberForm.html', {'error' : 'Error: Yo, the project does exist'})
				new_project = models.Project(name=form.cleaned_data['name'], description=form.cleaned_data['description'], programmingLang=form.cleaned_data['programmingLang'], yearsRequired=form.cleaned_data['yearsRequired'], speciality=form.cleaned_data['speciality'], company=request.user.engineer.company, created_at=form.cleaned_data['created_at'], updated_at=form.cleaned_data['updated_at'])
				new_project.save();
				context = {
					'projects' : new_project,
				}
				return render(request, 'project.html', context)
		else:
			form = forms.GroupForm()
		return render(request, 'projects.html')
		# render error page if user is not logged in
	return render(request, 'autherror.html')

def getCreateForm(request):
	if request.user.is_authenticated():
		return render(request, 'createProjectForm.html')
    # render error page if user is not logged in
	return render(request, 'autherror.html')