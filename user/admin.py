from django.contrib import admin
from .models import Shoppingcart
from .models import Order

# Register your models here
admin.site.register(Shoppingcart)
admin.site.register(Order)