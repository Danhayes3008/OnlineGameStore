from django.db import models

class  Device(models.Model):
    name = models.CharField(max_length=250)

class Product(models.Model):
    name = models.CharField(max_length=250, null=True, blank=False)
    device = models.OneToOneField(Device, on_delete=models.CASCADE, related_name='Device', null=True, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=7, null=True, blank=False)
    decription = models.CharField(max_length=500, null=True, blank=False)
    releaseDate = models.DateField(auto_now=False, null=True, blank=True)
    
