from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 50)
    product_desc = models.CharField(max_length=300)
    date = models.DateField()
    category = models.CharField(max_length=300 , default="")
    sub_category = models.CharField(max_length=300,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='store/images',default="")

    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=2000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=2000)
    email=models.CharField(max_length=2000)
    address=models.CharField(max_length=2000)
    city=models.CharField(max_length=2000)
    state=models.CharField(max_length=2000,default="")
    zip=models.CharField(max_length=2000)
    phone=models.CharField(max_length=2000,default="")

    def __str__(self):
        return self.name
