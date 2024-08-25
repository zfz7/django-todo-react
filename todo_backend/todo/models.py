from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TranslatedTask(models.Model):
    title = models.CharField(max_length=200)
    translatedTitle = models.CharField(max_length=200)
    description = models.TextField(default="")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
