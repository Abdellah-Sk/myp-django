"""PortfolioDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from django.conf import settings
from django.conf.urls.static import static

from projects.views import index
from projects.views import projects
from projects.views import contact
from projects.views import details
from projects.views import error404
from projects.views import error500
from projects.views import success

handler404 = 'projects.views.error404'
handler500 = 'projects.views.error500'

urlpatterns = [
    path('', index, name='home'),
    path('projects', projects, name='projects'),
    path('error404', error404, name='error404'),
    path('error500', error500, name='error500'),
    re_path(r'^projects/(?P<id>[0-9]+)$', details, name='details'),
    path('contact', contact, name='contact'),
    path('admin', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
