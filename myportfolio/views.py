from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def resume(request):
    return render(request,'resume.html')

def Blog(request):
    blogs=blog.objects.all()
    return render(request,'blog.html',{'blogs':blogs})

