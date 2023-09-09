from django.db import models
from product.models import Product
import datetime

class Shoppingcart(models.Model):
    user = models.CharField(max_length=32)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.CharField(max_length=32, default=1)
    last_modified = models.CharField(max_length=32, default=str(datetime.datetime.now())[:19])

    def __str__(self):
        return f"購物車: {self.id}"
    
    def return_users_order_same_product(username, product):
        return Shoppingcart.objects.get(user = username, product = product)
    
    def update_number(self, name, prod, sum):
        Shoppingcart.objects.filter(user = name, product = prod).update(number = sum)
    
    def delete_product(self, name, prod):
        Shoppingcart.objects.filter(user = name, product = prod).delete()

class Order(models.Model):
    user = models.CharField(max_length=32)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.CharField(max_length=32, default=1)
    time_created = models.CharField(max_length=32, default="伺服器時間: " + str(datetime.datetime.now()))
    isApproved = models.CharField(max_length=16, default="否")
    address = models.TextField(max_length=32, default="未輸入(不受理無地址訂單，請刪除此訂單並重新寄送)")
    timezone = models.CharField(max_length=20, default="UTC +0")

    def __str__(self):
        return f"訂單: {self.id}"
    
    def send_order(username, product, number, address, time, timezone):
        Order.objects.create(user = username, product = product, 
        number = number, address = address, time_created = time, timezone = timezone)
    
    def delete_order(username, product, id):
        Order.objects.filter(user = username, product = product, id = id).delete()

# class Id_test(models.Model):
#     my_id = models.IntegerField(max_length=32, default=0)
#     name = models.CharField(max_length=32, default=0)

# class Latest_id(models.Model):
#     latest_id = models.IntegerField(max_length=32, default=0)
#     name = models.CharField(max_length=32, default=0)