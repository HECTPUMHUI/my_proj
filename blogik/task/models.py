from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True) # can be empty
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=True)
