from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Project
from .form import ContactForm


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
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    return render(request, "projects/contact.html", {'form': form})


def error(request):
    return render(request, "projects/error404.html")


def success(request):
    return HttpResponse('Success! Thank you for your message.')
