from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Catalog

def home(request):
    params = {
        'phrase': 'Самый лучший магазин цветов'
    }
    return render(request, 'home.html', context=params)


def catalog(request):
    data = Catalog.objects.all()
    return render(request, 'catalog.html', {'catalog': data})

def product(request, id):
    data = {
        'catalog': id
    }
    return render(request, 'product.html',  data)