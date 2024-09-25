from django.db import models

# Create your models here.

class contactdb(models.Model):
    CONTACTNAME=models.CharField(max_length=100,null=True,blank=True)
    CONTACTEMAIL=models.EmailField(max_length=100,null=True,blank=True)
    CONTACTSUBJECT = models.EmailField(max_length=100, null=True, blank=True)
    CONTACTMESSAGE = models.CharField(max_length=100, null=True, blank=True)
    CONTACTPHONE = models.IntegerField(null=True, blank=True)

class Registerdb(models.Model):
    REGISTERNAME=models.CharField(max_length=100,null=True,blank=True)
    REGISTEREMAIL=models.EmailField(max_length=100,null=True,blank=True)
    REGISTERPASSWORD = models.CharField(max_length=100, null=True, blank=True)
    REGISTERCONFIRMPASSWORD = models.CharField(max_length=100, null=True, blank=True)

class cartdb(models.Model):
    USERNAME=models.CharField(max_length=100,null=True,blank=True)
    PRODUCTNAME=models.CharField(max_length=100,null=True,blank=True)
    QUANTITY=models.IntegerField(null=True,blank=True)
    TOTALPRICE=models.IntegerField(null=True,blank=True)
class Orderdb(models.Model):
    BILLINGNAME=models.CharField(max_length=100,null=True,blank=True)
    BILLINGEMAIL = models.EmailField(max_length=100, null=True, blank=True)
    BILLINGADDRESS = models.CharField(max_length=100, null=True, blank=True)
    BILLINGPHONE = models.IntegerField( null=True, blank=True)
    BILLINGPRICE = models.IntegerField( null=True, blank=True)
    BILLINGMESSAGE = models.CharField(max_length=100, null=True, blank=True)

