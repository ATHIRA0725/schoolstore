from django.db import models

# Create your models here.

class Formtable(models.Model):
    username=models.CharField(max_length=30)
    dob=models.DateField()
    age=models.IntegerField()
    mailid=models.EmailField()
    mobile=models.IntegerField()
    adrs=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    
