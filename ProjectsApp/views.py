"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render

from . import models

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
		projects_list = models.Project.objects.all()
		return render(request, 'projects.html', {
    	  	'projects': projects_list,
    	})
	return render(request, 'autherror.html')
	