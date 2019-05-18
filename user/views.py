from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from . models import Saran

class UserCreateView(CreateView):
    model = User
    email = ['email']
    template_name = "user/register.html"
    fields = ['username', 'email', 'first_name', 'last_name', 'password']
    
    def get_success_url(self):
        return reverse('index')

class UserUpdateView(UpdateView):
    model = User
    template_name = "user/update_profile.html"
    fields = ['username', 'email', 'first_name', 'last_name']

class SaranView(CreateView):
    model = Saran
    template_name = 'user/saran.html'
    fields = ['dari', 'sarans']
    
    def get_success_url(self):
        return reverse('saran')