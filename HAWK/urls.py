from django.urls import path
from . import views as HAWK_views
from .views import Team_Info, Team_Info_Detail, SponsorList, SponsorDetail

urlpatterns = [
    path('', Team_Info.as_view(), name='HAWK-Cars' ),
    path('team_baja/<car_number>/', HAWK_views.Team_Details, name='HAWK-Team' ),
    path('<int:pk>/', Team_Info_Detail.as_view(), name='HAWK-Team_Info_Detail'),
    path('sponsors/<car_number>/', SponsorList, name='HAWK-Sponsors'),
    path('sponsors/<car_number>/<int:id>/', SponsorDetail, name='HAWK-AboutSponsor'),
]
