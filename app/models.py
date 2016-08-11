from django.db import models

# Create your models here.

class contactus(models.Model):
    name=models.CharField(unique=False, max_length=100)
    email=models.CharField(unique=False, max_length=100)
    phone=models.CharField(unique=False, max_length=100)
    message=models.TextField(unique=False, max_length=500)

    def __unicode__(self):
        return  self.name
