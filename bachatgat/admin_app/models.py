from django.contrib.auth.models import User
from django.db import models

class profile(models.Model):
    name = models.CharField(max_length=100)
    account_no = models.CharField(max_length=100)
    aadhar_no = models.CharField(max_length=100)
    pan_no = models.CharField(max_length=100,default='Your Default Address')
    email = models.EmailField(max_length=100,default='Your Default Address')
    mobile = models.CharField(max_length=100,default='Your Default Address')
    username = models.CharField(max_length=100,default='Your Default Address')
    password = models.CharField(max_length=100,default='Your Default Address')
    birthday = models.DateField()
    address = models.CharField(max_length=100,default='Your Default Address')
    city = models.CharField(max_length=100,default='Your Default Address')
    state = models.CharField(max_length=100,default='Your Default Address')
    zip = models.CharField(max_length=100,default='Your Default Address')

    def __str__(self):
        return self.name
    
#class accounts(models.Model):

