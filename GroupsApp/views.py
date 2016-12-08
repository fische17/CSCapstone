"""GroupsApp Views
Created by Naman Patwari on 10/10/2016.
"""
from django.shortcuts import render

from . import models
from . import forms
<<<<<<< f0f1b5affaa26737f38bf84e58114241d6952d74
from CommentsApp.models import Comment
=======
import itertools
>>>>>>> Suggestion Algorithm

def getGroups(request):
    if request.user.is_authenticated():
        groups_list = models.Group.objects.all()
        context = {
            'groups' : groups_list,
        }
        return render(request, 'groups.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        is_member = in_group.members.filter(email__exact=request.user.email)
        context = {
            'group' : in_group,
            'userIsMember': is_member,
        }
        return render(request, 'group.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroupForm(request):
    if request.user.is_authenticated():
        return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroupFormSuccess(request):
    if request.user.is_authenticated():
        if request.user.is_student:
            if request.method == 'POST':
                form = forms.GroupForm(request.POST)
                if form.is_valid():
                    if models.Group.objects.filter(name__exact=form.cleaned_data['name']).exists():
                        return render(request, 'groupform.html', {'error' : 'Error: That Group name already exists!'})
                    new_group = models.Group(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
                    new_group.save()
                    context = {
                        'name' : form.cleaned_data['name'],
                    }
                    return render(request, 'groupformsuccess.html', context)
            else:
                form = forms.GroupForm()
            return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def joinGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        in_group.members.add(request.user)
        in_group.save();
        request.user.group_set.add(in_group)
        request.user.save()
        context = {
            'group' : in_group,
            'userIsMember': True,
        }
        return render(request, 'group.html', context)
    return render(request, 'autherror.html')

def unjoinGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        in_group.members.remove(request.user)
        in_group.save();
        request.user.group_set.remove(in_group)
        request.user.save()
        context = {
            'group' : in_group,
            'userIsMember': False,
        }
        return render(request, 'group.html', context)
    return render(request, 'autherror.html')

def addMemberGroup(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.AddMembersForm(request.POST)
            if form.is_valid():
                in_user_email = form.cleaned_data['email']
                if not models.MyUser.objects.filter(email__exact=in_user_email).exists():
                    return render(request, 'addMemberForm.html', {'error' : 'Error: The user does not exist'})
                
                in_user = models.MyUser.objects.get(email__exact=in_user_email)
                in_group_name = request.GET.get('name', "None")
                in_group = models.Group.objects.get(name__exact=in_group_name)
                in_group.members.add(in_user)
                in_group.save();
                in_user.group_set.add(in_group)
                in_user.save()
                context = {
                    'group' : in_group,
                    'userIsMember': True,
                }
            return render(request, 'group.html', context)
        else:
            form = forms.GroupForm()
        return render(request, 'group.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def helloWorld(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        return render(request, 'addMemberForm.html', {
    	    'group': in_group,
    	})
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def addProjectGroupSuccess(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.addProjectForm(request.POST)
            if form.is_valid():
                in_projectName = form.cleaned_data['projectName']
                if not models.Project.objects.filter(name__exact=in_projectName).exists():
                    return render(request, 'addMemberForm.html', {'error' : 'Error: Yo, the project does not exist'})
                
                in_project = models.Project.objects.filter(name__exact=in_projectName)
                in_group_name = request.GET.get('name', "None")
                in_group = models.Group.objects.get(name__exact=in_group_name)
                in_group.project = in_project[0]
                in_group.save();
                context = {
                    'group' : in_group,
                    'userIsMember': True,
                }
                return render(request, 'group.html', context)
        else:
            form = forms.GroupForm()
        return render(request, 'group.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getAddProject(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        return render(request, 'addProjectForm.html', {
            'group': in_group,
        })
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def comment(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        return render(request, 'groupCommentForm.html', {
            'group': in_group,
        })

def addComment(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.groupCommentForm(request.POST)
            if form.is_valid():
                in_name = request.GET.get('name', 'None')
                print(in_name)
                in_group = models.Group.objects.get(name__exact=in_name)
                new_comment = Comment(comment=form.cleaned_data['comment'])
                new_comment.group = in_group
                new_comment.poster = request.user
                new_comment.save()
                in_group.comments.add(new_comment)
                return render(request, 'group.html', {
                    'group': in_group,
                })
    return render(request, 'autherror.html')

def deleteComment(request):
    if request.user.is_authenticated(): 
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        in_comment_id = request.GET.get('comment', 'None')
        in_comment = Comment.objects.get(id=in_comment_id)
        in_comment.delete()
        print(in_comment.comment)
        return render(request, 'group.html', {
            'group': in_group,
        })

def suggestProjectForGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        in_members = in_group.members.all()
        values = []
        for member in in_members:
            if member.is_student:
                y = member.student.languages.strip().split(",")
                for word in y:
                    values.append(word)
            
        output = []
        seen = set()
        for value in values:
            if value not in seen:
                output.append(value)
                seen.add(value)
        
        projects_list = models.Project.objects.filter(programmingLang__contains="asdasdjwk")
			
        for lang in output:
            projects_list = itertools.chain(projects_list, models.Project.objects.filter(programmingLang__exact=lang))
        
        return render(request, 'groupSuggestedProjects.html', {
            'projects': projects_list,
        })
    # render error page if user is not logged in
    return render(request, 'autherror.html')  

def removeDups(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    print(output)
    return output

def RemoveProject(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        in_group.project = None
        in_group.save()
        return render(request, 'groupRemoveProjectSuccess.html', {
            'group': in_group,
            'name': in_group.name
        })
    # render error page if user is not logged in
    return render(request, 'autherror.html')