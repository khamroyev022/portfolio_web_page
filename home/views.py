from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    context = {
        
    }
    render(request, 'home.html' ,context)