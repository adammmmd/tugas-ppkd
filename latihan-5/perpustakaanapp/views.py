# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())

def collections(request):
    template = loader.get_template('collections.html')
    return HttpResponse(template.render())












