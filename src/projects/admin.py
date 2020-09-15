from django.contrib import admin

from .models import Project
from .models import Technology

admin.site.register(Project)
admin.site.register(Technology)


