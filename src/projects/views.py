from django.shortcuts import render

def index(request):
    return render(request, "projects/index.html")

def projects(request):
    return render(request, "projects/projects.html")

def contact(request):
    return render(request, "projects/contact.html")