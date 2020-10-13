from django.contrib import admin

from .models import Project
from .models import Technology
from .models import Contact
from .models import Profile

admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(Contact)
admin.site.register(Profile)



