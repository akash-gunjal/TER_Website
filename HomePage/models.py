from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class SlideShow(models.Model):
    image = models.ImageField(default='default.jpg', upload_to ='SlideShow')


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    def __str__(self):
        return self.type
