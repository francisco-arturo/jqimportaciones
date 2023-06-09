from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from .models import Product, Category
import csv
from .forms import CsvUploadForm
import io

def homepage(request):
    products = Product.objects.all()
    for product in products:
        product.image = product.image.split(',')[0] if product.image else None
    return render(request, 'homepage.html', {'products': products})

def product_detail(request, sku):
    product = get_object_or_404(Product, sku=sku)
    images = product.image.split(',')
    return render(request, 'product.html', {'product': product, 'images': images})

def csv_upload(request):
    if request.method == 'POST':
        form = CsvUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            category = form.cleaned_data['category']
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            reader = csv.DictReader(io_string)

            for row in reader:
                product = Product.objects.create(
                    sku=row.get('SKU'),
                    name=row.get('Name'),
                    description=row.get('Description'),
                    price=row.get('Price'),
                    image=row.get('Images'),
                    category=category
                )
            messages.success(request, 'CSV file has been uploaded and processed.')
    else:
        form = CsvUploadForm()
    return render(request, 'csv_upload.html', {'form': form})
