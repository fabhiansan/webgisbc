from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def landingpage(request):
    return render(request, 'users/landingpage.html')



@login_required(login_url='login')
def home(request):
    return render(request, 'users/home.html')



def CreateUser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form' : form
    }
    return render(request, 'users/register.html', context)

