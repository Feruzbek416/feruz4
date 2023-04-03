from django.shortcuts import render
from .models import *
# Create your views here.

def blog(request):
    context = Blog.objects.all()
    return render(request,'ap/home.html',{"context":context})

def detail(request,name):
    obj = Blog.objects.get(name=name)
    Author1 = Author.objects.all()
    return render(request,'ap/detail.html',{"obj":obj,"Author":Author1})