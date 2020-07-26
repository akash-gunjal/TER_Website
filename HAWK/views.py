from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Team_Members, Team, Team_Sponsors
from django.views.generic import (
     ListView,
     DetailView,
     CreateView,
     UpdateView,
     DeleteView
)


class Team_Info(ListView):
    model = Team
    context_object_name = 'teams'
    template_name = 'HAWK/Team_Info.html'

class Team_Info_Detail(DetailView):
    model = Team
    template_name = 'HAWK/Team_Info_Detail.html'

#team members 
def Team_Details(request, car_number):
        context={
           'members':Team_Members.objects.filter(team__car_number = car_number).order_by('Post_In_Team','Post_In_Subsystem','Subsystem'),
           'incharge_members':['Captain','Captain and Driver','Vice-Captain',
                               'Vice-Captain and Driver','Project Manager',
                                'Project Manager and Driver'],
           'subsystems':['Transmission','Suspension','Steering','Brakes', 'Rollcage','Project Management']
        }
        return render(request, 'HAWK/Team_Members.html', context)

def SponsorList(request, car_number):
    context = {
               'Sponsorship_Packages' : ['Platinum','Gold','Silver','Bronze'],
               'Sponsors': Team_Sponsors.objects.filter(team__car_number = car_number)
               }
    return render(request, 'HAWK/Sponsors.html', context)

def SponsorDetail(request, car_number, id):
    context = {
               'object': Team_Sponsors.objects.filter(id = id).first()
               }
    return render(request, 'HAWK/AboutSponsor.html', context)
