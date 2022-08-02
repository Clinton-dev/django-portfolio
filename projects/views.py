from urllib import request
from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/index.html', context)

def portfolio_details(request,pk):
    project = Project.objects.get(id=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/details.html', context)