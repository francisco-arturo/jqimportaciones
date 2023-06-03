from django.shortcuts import get_object_or_404, render
from .models import Product

def homepage(request):
    products = Product.objects.all()
    return render(request, 'homepage.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    images = product.image.split(',')
    return render(request, 'product.html', {'product': product, 'images': images})
