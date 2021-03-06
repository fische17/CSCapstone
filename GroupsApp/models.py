"""GroupsApp Models

Created by Naman Patwari on 10/10/2016.
"""
from django.db import models
from AuthenticationApp.models import MyUser
from ProjectsApp.models import Project

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    members = models.ManyToManyField(MyUser)
    comments = models.ManyToManyField('CommentsApp.Comment', related_name='comments')
    project = models.ForeignKey(Project, null= True, blank=True, related_name='project')

    
    def __str__(self):
        return self.name