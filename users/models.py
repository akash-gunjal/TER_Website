from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime
from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.conf.urls import include, url
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
    SUBSYSTEMS=(('Transmission','Transmission'),('Suspension','Suspension'),
                ('Steering','Steering'), ('Brakes', 'Brakes'),
                ('Rollcage','Rollcage'),('Project Management','Project Management'),('None','None'))
    PostInTeam=(('Captain','Captain'),('Captain and Driver','Captain and Driver'),('Vice-Captain','Vice-Captain'),
                ('Vice-Captain and Driver','Vice-Captain and Driver'),('Project Manager', 'Project Manager'),
                ('Project Manager and Driver', 'Project Manager and Driver'),('Driver','Driver'),
                ('Codriver','Codriver'),('Tier-1 Member','Tier-1 Member'),
                 ('Tier-2 Member','Tier-2 Member'), ('None','None'))
    PostInSubsystem = (('Head','Head'),('Senior Member','Senior Member'), ('Member','Member'), ('None','None'))
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to ='profile_pics')
    Post_In_Team = models.TextField( choices=PostInTeam, default='None')
    Subsystem = models.TextField(choices=SUBSYSTEMS, default='None')
    Post_In_Subsystem = models.TextField( choices=PostInSubsystem, default='None')
    PhoneNumber= models.IntegerField(default=0)
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img= Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
