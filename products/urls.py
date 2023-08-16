from rest_framework import routers
from .views import ProductsViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')
