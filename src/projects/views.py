from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, "projects/index.html", {'projects': projects})


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {'projects': projects})


def details(request, id):
    project = Project.objects.all()
    return render(request, "projects/details.html", {'project': project[int(id)-1]})


def contact(request):
    return render(request, "projects/contact.html")


def error(request):
    return render(request, "projects/error404.html")
