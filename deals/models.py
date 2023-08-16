from django.db import models
from products.models import Product


class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name='ordered_product', on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name + ' / ' + str(self.amount) + ' units'


class Order(models.Model):
    products = models.ManyToManyField(OrderItem, related_name='order')

