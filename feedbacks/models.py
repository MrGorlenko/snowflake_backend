from django.db import models


class ContactUsForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return 'Email: ' + self.email + ' | Name: ' + self.name