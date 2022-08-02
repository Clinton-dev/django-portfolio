from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    print(projects)
    return render(request, 'projects/index.html', context)