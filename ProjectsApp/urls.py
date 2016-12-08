"""ProjectsApp URL Configuration

Created by Harris Christiansen on 10/02/16.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^project/all$', views.getProjects, name='Projects'),
    url(r'^project$', views.getProject, name='Project'),
    url(r'^project/bookmarks$', views.getBookmarks, name='Bookmarks'),
    url(r'^project/bookmark$', views.bookmarkProject, name='Bookmarked'),
    url(r'^project/suggested$', views.getSuggestedProjects, name='Suggested'),
    url(r'^project/formsuccess$', views.getProjectFormSuccess, name='ProjectFormSuccess'),
    url(r'^project/createForm$', views.getCreateForm, name='ProjectCreateForm'),
]
