from django.db import models


# Create your models here.
class Region(models.Model):
    region_name =   models.CharField(max_length=264,unique=True)   
    def __str__(self):
        return self.region_name

class Province(models.Model):
    region_id = models.ForeignKey(Region,on_delete=models.CASCADE)
    province_name = models.CharField(max_length=264, unique=True) 
    def __str__(self):
        return self.province_name

class Shop(models.Model):
    region_id = models.ForeignKey(Region,on_delete=models.CASCADE)
    province_id = models.ForeignKey(Province,on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=264,blank=False, null=False) 
    phonenmuber = models.CharField(max_length=20,blank=True, null=True) 
    level = models.CharField(max_length=1,blank=False, null=False) 
    transpot = models.CharField(max_length=264,blank=True, null=True) 
    def __str__(self):
        return self.shop_name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    region_id = models.ForeignKey(Region,on_delete=models.CASCADE)
    province_id = models.ForeignKey(Province,on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    def __nonzero__(self):
        return self.id

class OrderImage(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='uploads') 

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.CharField(max_length=264) 
    cost = models.IntegerField(blank=False, null=False)
    number = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)