from .serializers import ContactUsFormSerializer
from .models import ContactUsForm
from rest_framework.viewsets import ModelViewSet

class ContactUsViewSet(ModelViewSet):
    model = ContactUsForm
    serializer_class = ContactUsFormSerializer
    queryset = ContactUsForm.objects
