"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models
from AuthenticationApp.models import MyUser
from CompaniesApp.models import Company

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    programmingLang = models.CharField(max_length=100, null=True)
    yearsRequired = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    company = models.ForeignKey(Company, null= True, blank=True)
    def __str__(self):
        return self.name

class Bookmark(models.Model):
    user_id = models.OneToOneField(MyUser)
    project_id = models.OneToOneField(Project)

    def __str__(self):
        return self.project_id.name
