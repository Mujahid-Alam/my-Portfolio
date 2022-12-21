from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='upload/')
    live = models.CharField(max_length=200 ,null=True, blank=True)
    github = models.CharField(max_length=200, null=True, blank=True)
