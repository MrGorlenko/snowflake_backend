from rest_framework import routers
from .views import OrderViewSet, OrderItemViewSet


router = routers.DefaultRouter()
router.register(r'order-item', OrderItemViewSet, basename='order-item')
router.register(r'order', OrderViewSet, basename='order')
