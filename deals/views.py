from .serializers import OrderItemSerializer, OrderSerializer
from .models import Order, OrderItem
from rest_framework.viewsets import ModelViewSet


class OrderItemViewSet(ModelViewSet):
    model = OrderItem
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects


class OrderViewSet(ModelViewSet):
    model = Order
    serializer_class = OrderSerializer
    queryset = Order.objects
