from django.db import models

from django.conf import settings


class Address(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    number_flat = models.CharField(max_length=10, blank=True)


class Property(models.Model):
    title = models.CharField(max_length=100)
    type_property = models.CharField(max_length=50)
    price = models.IntegerField()
    area = models.IntegerField()
    rooms = models.IntegerField()
    desciption = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Item(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    pub_date = models.DateField()
    type_rent = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20, blank=True)
