from django.shortcuts import render

def index(request):
    return render('projects/index.html')