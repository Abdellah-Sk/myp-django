from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Technology(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True)
    excerpt = models.TextField(null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='img')
    repo_url = models.CharField(max_length=255)
    website_url = models.CharField(max_length=255, blank=True)
    pub_date = models.DateTimeField('date published')
    technology = models.ManyToManyField(Technology)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.user)



