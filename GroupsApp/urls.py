"""GroupsApp URL

Created by Naman Patwari on 10/10/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^group/all$', views.getGroups, name='Groups'),
	url(r'^group/form$', views.getGroupForm, name='GroupForm'),
    url(r'^group/formsuccess$', views.getGroupFormSuccess, name='GroupFormSuccess'),
    url(r'^group/join$', views.joinGroup, name='GJoin'),
    url(r'^group/unjoin$', views.unjoinGroup, name='GUnjoin'),
    url(r'^group$', views.getGroup, name='Group'),
    url(r'^group/addMember', views.addMemberGroup, name='AddMemberGroup'),
    url(r'^group/helloWorld', views.helloWorld, name='helloWorld'),
    url(r'^group/addProject', views.getAddProject, name='AddProject'),
    url(r'^group/AddProjectSuccess', views.addProjectGroupSuccess, name='AddProjectSuccess'),
    url(r'^group/comment', views.comment, name='Comment'),
    url(r'^group/addGroupComment', views.addComment, name='Comment'),
    url(r'^group/deleteComment', views.deleteComment, name='DeleteComment'),
]