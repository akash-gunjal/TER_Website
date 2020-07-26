from django.urls import path
from . import views as homepage_views

urlpatterns = [
    path('', homepage_views.Home, name='Home-Page' ),
    path('about/', homepage_views.About, name='HomePage-About' ),
]
