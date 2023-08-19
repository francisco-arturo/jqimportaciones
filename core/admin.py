from django.contrib import admin
from .models import Category, Product, Order, OrderItem, ExchangeRate

class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('id', 'rate_to_pesos')
    list_editable = ('rate_to_pesos',)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ExchangeRate, ExchangeRateAdmin)