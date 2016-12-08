"""ProjectApp Forms

Created by Naman Patwari on 10/10/2016.
"""
from django import forms

class ProjectForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    description = forms.CharField(label='Description', max_length=10000)
    programmingLang = forms.CharField(label='ProgrammingLanguage',max_length=100)
    yearsRequired = forms.CharField(label='YearsRequired', max_length=100)
    speciality = forms.CharField(label='Speciality', max_length=100)
    created_at = forms.DateTimeField(label="Date created at")
    updated_at = forms.DateTimeField(label="Date updated at")
