from django.db import models
from django.contrib.auth.models import User
from datetime import*


# Create your models here.
class Formalshirt(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(upload_to="gallery")
    description=models.TextField(max_length=500,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s' %(self.name)
class Tshirt(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=500,blank=True)
    def __str__(self):
        return '%s' %(self.name)
class Shirts(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(upload_to="gallery")
    description=models.TextField(max_length=500,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s' %(self.name)
