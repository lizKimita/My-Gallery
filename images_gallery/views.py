from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image, Category, Location

# Create your views here.
def all_images(request):
    image = Image.get_images()
    title = "gallery"
    
    return render(request, 'all_images/gallery.html', {"title":title, "image":image})