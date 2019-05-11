from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image, Category, Location

# Create your views here.
def all_images(request):
    image = Image.get_images()
    title = "gallery"
    
    return render(request, 'all_images/gallery.html', {"title":title, "image":image})

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all_images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image Category"
        return render(request, 'all_images/search.html',{"message":message})