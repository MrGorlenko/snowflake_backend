from rest_framework import serializers
from .models import ContactUsForm


class ContactUsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsForm
        fields = '__all__'
