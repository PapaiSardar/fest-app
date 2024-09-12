from django.shortcuts import render,redirect
from django.http import HttpResponse
from fest_app.models import *



# Create your views here. 
def events(request):
    return render (request,'events.html')



def home(request):
    return render(request,'index.html')


def photos(request):
    return render(request, 'gallery.html')










 
























    
