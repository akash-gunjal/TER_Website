from django.shortcuts import render
from .models import SlideShow, Blog
from django.contrib.auth.models import User


def Home(request):
    context={
       'SlideShow':SlideShow.objects.all()
    }
    return render(request, 'HomePage/SlideShow.html', context)

def About(request):
    context={
       'object':Blog.objects.filter(type='ABOUT').first()
    }
    return render(request, 'HomePage/About.html', context)
