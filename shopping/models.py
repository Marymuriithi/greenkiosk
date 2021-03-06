from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from catalogue.models import Product
from customers.models import Customer

class Cart(models.Model):
    products = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status

class Order(models.Model):
    order_number = models.IntegerField()
    date_placed = models.DateTimeField()
    status = models.CharField(max_length=60)
    basket = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True)
    customer =models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    delivery_time = models.DateTimeField()
    shipping_provider = models.ForeignKey('shipping.ShippingProvider', on_delete=models.CASCADE,null=True)
    order_price = models.DecimalField(max_digits=6, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.order_number

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    payment_method = models.CharField(max_length=50)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date_of_payment = models.DateTimeField()

    def __str__(self):
        return self.customer.get_full_name
