from django.db import models

# Create your models here.
class categorydb(models.Model):

    CATEGORYNAME=models.CharField(max_length=100,null=True,blank=True)
    CATEGORYDESCRIPTION = models.CharField(max_length=100, null=True, blank=True)
    CATEGORYIMAGE = models.ImageField(upload_to="productimage", null=True, blank=True)

class productdb(models.Model):
    CATEGORY=models.CharField(max_length=100,null=True,blank=True)
    PRODUCTNAME = models.CharField(max_length=100, null=True, blank=True)
    PRODUCTPRICE = models.IntegerField( null=True, blank=True)
    PRODUCTDESCRIPTION = models.CharField(max_length=100, null=True, blank=True)
    PRODUCTIMAGE = models.ImageField(upload_to="productimages", null=True, blank=True)
