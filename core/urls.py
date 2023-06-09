from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('product/<int:sku>/', views.product_detail, name='product_detail'),
    path('csv_upload/', views.csv_upload, name='csv_upload'),
]
