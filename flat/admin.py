from django.contrib import admin
from .models import Property, Item, Address, Profile

# Register your models here.

admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(Address)
admin.site.register(Property)
