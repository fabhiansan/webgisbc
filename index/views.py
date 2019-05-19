from django.shortcuts import render, render_to_response

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


import os 

def fotoudara(request):
    path="D:\webgisbalangan\webgisbalangan\index\static\media\\fotoudara"  # insert the path to your directory   
    file_list = os.listdir(path)   
    return render(request, 'index/fotoudara.html', {'files': file_list})