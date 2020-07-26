from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.files.storage import FileSystemStorage

class Team(models.Model):
    car_number = models.IntegerField(default  = 0)
    technical_highlights = models.TextField(default = 'None')
    acheivements = models.TextField(default = 'None')
    #image = models.ImageField(default='default.jpg', upload_to ='cars/Car_Images')
    def __str__(self):
            return f'Hawk {self.car_number} '

class Team_Members(models.Model):
    SUBSYSTEMS=(('Transmission','Transmission'),('Suspension','Suspension'),
                ('Steering','Steering'), ('Brakes', 'Brakes'),
                ('Rollcage','Rollcage'),('Project Management','Project Management'),('None','None'))
    PostInTeam=(('Captain','Captain'),('Captain and Driver','Captain and Driver'),('Vice-Captain','Vice-Captain'),
                ('Vice-Captain and Driver','Vice-Captain and Driver'),('Project Manager', 'Project Manager'),
                ('Project Manager and Driver', 'Project Manager and Driver'),('Driver','Driver'),
                ('Codriver','Codriver'),('Tier-1 Member','Tier-1 Member'),
                 ('Tier-2 Member','Tier-2 Member'), ('None','None'))
    first_Name = models.CharField(verbose_name="First Name", max_length=20, default='None')
    Middle_Name = models.CharField(verbose_name="Middle Name", max_length=20, default='None')
    last_Name = models.CharField(verbose_name="Last Name", max_length=20, default='None')
    address = models.TextField(max_length=200, verbose_name="Address", default='None')
    PostInSubsystem = (('Head','Head'),('Senior Member','Senior Member'), ('Member','Member'), ('None','None'))
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to ='HAWK/TeamMembers')
    Post_In_Team = models.TextField( choices=PostInTeam, default='None')
    Subsystem = models.TextField(choices=SUBSYSTEMS, default='None')
    Post_In_Subsystem = models.TextField( choices=PostInSubsystem, default='None')
    PhoneNumber= models.IntegerField(default=0)
    EmailId = models.EmailField(default = 'none')

    def __str__(self):
        return f'Hawk {self.team.car_number} Member {self.first_Name}'
"""
    def save(self, *args, **kawrgs):

        img= Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
"""

class Images(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Image', upload_to="HAWK/images", default='default.jpg')
    def __str__(self):
            return f'Hawk {self.team.car_number} image'


class Team_Sponsors(models.Model):
    Sponsor_type = (('Platinum','Platinum'),( 'Gold', 'Gold') ,('Silver','Silver'), ('Bronze','Bronze'))
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to ='HAWK/Sponsors')
    name = models.CharField(max_length=50, default="None")
    about_Sponsor_in_short = models.CharField(max_length=100, default="None")
    about_Sponsor = models.TextField(default="None")
    Sponsorship_Package = models.CharField(max_length=10, choices=Sponsor_type ,default= 'Gold')
    Link_Website = models.CharField(max_length=250, default='None')
    Link_Instagram = models.CharField(max_length=250, default='None')
    Link_Facebook = models.CharField(max_length=250, default='None')
    Link_Twitter = models.CharField(max_length=250, default='None')
    def __str__(self):
            return f'Hawk {self.team.car_number} Sponsor {self.name}'
