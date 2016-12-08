"""GroupsApp Forms

Created by Naman Patwari on 10/10/2016.
"""
from django import forms

class GroupForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    description = forms.CharField(label='Description', max_length=300)

class AddMembersForm(forms.Form):
	email = forms.CharField(label="Email", max_length=200)

class addProjectForm(forms.Form):
    projectName = forms.CharField(label="projectName", max_length=200)

class groupCommentForm(forms.Form):
    comment = forms.CharField(label='Text', max_length=500)