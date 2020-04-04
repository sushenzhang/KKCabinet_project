"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Pic,Material,Color,Classify


def home(request):
    """Renders the home page."""
    pictures_on_home = Pic.objects.filter(is_on_home_page=True)
    pictures_on_home_gallery = Pic.objects.filter(is_on_home_page_gallery=True)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'pics_home':pictures_on_home,
            'pics_gallery':pictures_on_home_gallery,
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def gallery(request):
    """Renders the gallery page."""
    assert isinstance(request, HttpRequest)
    pictures = Pic.objects.all()
    material = Material.objects.all()
    color = Color.objects.all()
    classify = Classify.objects.all()
    return render(
        request,
        'app/gallery.html',
        {
            'title':'gallery',
            'pics': pictures,
            'materials':material,
            'colors':color,
            'classifies':classify,
       
        }
    )

