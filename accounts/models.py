from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Transaction(models.Model):
    type = (('Expenditure','Expenditure'), ('Income','Income'))
    Income_Sources = (('Contri','Contri'),('Sponsorship','Sponsorship'),
             ('Extra From Team Member','Extra From Team Member'),
             ('College','College'), ('Prize Money', 'Prize Money'))
    Type = models.CharField(max_length=20, choices = type ,default= 'Expenditure')
    Expenditure_on = models.CharField(max_length=50 ,default= 'NA')
    Income_Source = models.CharField(max_length=50, choices = Income_Sources ,default= 'NA')
    Amount = models.IntegerField(default = 0)
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    class Debit(models.Model):
        Amount = models.IntegerField(default = 0)
    class Credit(models.Model):
        Amount = models.IntegerField(default = 0)
    def get_absolute_url(self):
        return reverse('Transaction-Detail', kwargs={'pk': self.pk})
