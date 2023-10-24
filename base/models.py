from django.db import models

class RegStu(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(null=None)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    
    