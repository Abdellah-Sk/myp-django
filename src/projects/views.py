from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Project
from .form import ContactForm


def index(request):
    projects = Project.objects.all()
    return render(request, "projects/index.html", {'projects': projects})


def projects(request):
    projects = list(reversed(Project.objects.all()))
    paginator = Paginator(projects, 5)  # Show 5 contacts per page.
    page = request.GET.get('page', 1)

    try:
        x = paginator.page(page)
    except PageNotAnInteger:
        x = paginator.page(1)
    except EmptyPage:
        x = paginator.page(paginator.num_pages)

    return render(request, "projects/projects.html", {'x': x})


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
                x = EmailMessage(
                    subject='MYP Contact - ' + name,
                    body=message,
                    from_email='skoundriabdellah@gmail.com',
                    to=['skoundriabdellah@gmail.com'],
                    reply_to=[email],
                )
                x.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    return render(request, "projects/contact.html", {'form': form})


def error404(request, exception):
    return render(request, "projects/errors/error404.html", {}, status=404)


def error500(request):
    return render(request, "projects/errors/error500.html", {}, status=500)


def success(request):
    return HttpResponse('Success! Thank you for your message.')
