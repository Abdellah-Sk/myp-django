from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, "projects/index.html", {'projects':projects})

def projects(request):
    return render(request, "projects/projects.html")

def contact(request):
    return render(request, "projects/contact.html")