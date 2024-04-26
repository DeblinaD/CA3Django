from django.db import models
from datetime import date
from django.contrib.auth.hashers import make_password


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return self.username
    
class User(models.Model):     
    User_id= models.CharField(max_length= 10,primary_key=True)
    Name = models.CharField(max_length = 100)

    def _str_(self):
        return self.User_id


class Record(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField(default=date.today)
    Quantity = models.DecimalField(max_digits=6, decimal_places=2)
    Fat = models.DecimalField(max_digits=4, decimal_places=2)
    SNF = models.DecimalField(max_digits=4, decimal_places=2)
    Amount = models.DecimalField(max_digits = 10, decimal_places=4)