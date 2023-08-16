from django.db import models


class Product(models.Model):
    spine = models.ImageField()
    book = models.ImageField()
    bottle = models.ImageField()
    brunch = models.ImageField()
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    volume = models.CharField(max_length=255)
    alcoholLevel = models.CharField(max_length=255)
    flavor = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

