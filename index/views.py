from django.shortcuts import render, redirect, reverse
from . models import Saran
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
# Create your views here.
def index(request):
    return render(request, 'index/index.html')

def mapviews(request):
    return render(request, 'index/mapviews.html')

def jquery(request):
    return render(request, 'index/learnjq.html')

def api(request):
    return render(request, 'index/map.html')

def dmsconverter(request):
    return render(request, 'index/dmsconverter.html')

def degreeconverter(request):
    return render(request, 'index/degreeconverter.html')

#def fotoudara(request):
#    return render(request, 'index/fotoudara.html')
class SaranView(CreateView):
    model = Saran
    template_name = 'index/saran.html'
    fields = ['dari', 'sarans']
    
    def get_success_url(self):
        return reverse('index')

import os 

from django.contrib.auth.decorators import user_passes_test

def loa_check(User):
    return User.profile.levelofaccess > 0

@user_passes_test(loa_check)
def fotoudara(request):
    path="D:\webgisbalangan\webgisbalangan\index\static\media\\fotoudara"  # insert the path to your directory   
    file_list = os.listdir(path)   
    return render(request, 'index/fotoudara.html', {'files': file_list})


#error handling
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings
from django.urls import path


def response_error_handler(request, exception=None):
    return HttpResponse('Error handler content', status=403)


def permission_denied_view(request):
    raise PermissionDenied
