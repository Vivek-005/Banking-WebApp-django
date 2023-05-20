from django.db import models

class customerdetails(models.Model):
    accno = models.IntegerField(default=0,primary_key=True)
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=150,null=True)
    amount = models.DecimalField(max_digits=8,decimal_places=2)

class transactionhistory(models.Model):
   sender = models.CharField(max_length=200,null=True)
   reciever = models.CharField(max_length=200,null=True)
   amount = models.IntegerField(default=0)
   date_trans = models.DateTimeField(auto_now_add=True)    
    
