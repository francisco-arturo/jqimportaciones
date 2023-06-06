from django.shortcuts import get_object_or_404, render
from .models import Product

def homepage(request):
    products = Product.objects.all()
    for product in products:
        product.image = product.image.split(',')[0] if product.image else None
    return render(request, 'homepage.html', {'products': products})

def product_detail(request, sku):
    product = get_object_or_404(Product, sku=sku)
    images = product.image.split(',')
    return render(request, 'product.html', {'product': product, 'images': images})
