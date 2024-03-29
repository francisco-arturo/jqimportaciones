from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    sku = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    def price_in_pesos(self):
        exchange_rate = ExchangeRate.objects.first()
        if exchange_rate:
            return self.price * exchange_rate.rate_to_pesos
        return None

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order: {self.id}'

class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Order Item: {self.id}'

class ExchangeRate(models.Model):
    rate_to_pesos = models.DecimalField(max_digits=4, decimal_places=0)

    @classmethod
    def set_current_rate(cls, new_rate):
        instance, created = cls.objects.get_or_create(pk=1)
        instance.rate_to_pesos = new_rate
        instance.save()