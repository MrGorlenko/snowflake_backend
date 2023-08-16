from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from rest_framework.viewsets import ModelViewSet


class ProductsViewSet(ModelViewSet):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects
