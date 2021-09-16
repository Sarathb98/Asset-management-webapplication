from django.db import models
from django.db import models


class Register(models.Model):
        name = models.CharField(max_length=30)
        email = models.CharField(max_length=30)
        addr = models.CharField(max_length=40)
        phno = models.IntegerField()
        uname = models.CharField(max_length=20)

class Login(models.Model):
        uname = models.CharField(max_length=20)
        paswd = models.CharField(max_length=15)
        type = models.IntegerField(2)

class Asset(models.Model):
        ide = models.CharField(max_length = 20)
        dev = models.CharField(max_length = 20)
        dep = models.CharField(max_length = 20)
        own = models.CharField(max_length = 20)
        loc = models.CharField(max_length = 20)
        sts = models.CharField(max_length = 20)
# Create your models here.
