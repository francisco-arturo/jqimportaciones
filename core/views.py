from django.shortcuts import render
from .models import Product

def homepage(request):
    products = Product.objects.all()
    return render(request, 'homepage.html', {'products': products})
