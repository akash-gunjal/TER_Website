from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.views.generic import (
     ListView,
     DetailView,
     CreateView,
     UpdateView,
     DeleteView
)

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST,)
        if form.is_valid():
            user = form.save()
            #user.is_active = False
            user.save()
            username=form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f'Account Has Been Created {username}!')
            authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})



@login_required
def profile(request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():

            messages.success(request, f'Account has been updated successfully!')
            username=u_form.cleaned_data.get('username')
            u_form.save()
            p_form.save()
            #user = get_object_or_404(User, username =username)
            #user.is_active= False
            #user.save()
            #return redirect('Home-Page')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context={
       'u_form': u_form,
       'p_form' : p_form
    }
    return render(request,'users/profile.html', context)
