from __future__ import unicode_literals

from django.db import models

# Create your models here.
class dance(models.Model):
    para1=models.TextField()
    para2=models.TextField()
    para3=models.TextField()
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    head1=models.CharField(max_length=120)
    head2=models.CharField(max_length=120)
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.BigIntegerField(blank=False)
    messege=models.TextField(blank=False)
    def __str__(self):
        return self.name

class music(models.Model):
    para1=models.TextField()
    para2=models.TextField()
    para3=models.TextField()
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    head1=models.CharField(max_length=120)
    head2=models.CharField(max_length=120)
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.BigIntegerField(blank=False)
    messege=models.TextField(blank=False)
    def __str__(self):
        return self.name


class quiz(models.Model):
    para1=models.TextField()
    para2=models.TextField()
    para3=models.TextField()
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    head1=models.CharField(max_length=120)
    head2=models.CharField(max_length=120)
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.BigIntegerField(blank=False)
    messege=models.TextField(blank=False)
    def __str__(self):
        return self.name


class sankalp(models.Model):
    para1=models.TextField()
    para2=models.TextField()
    para3=models.TextField()
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    head1=models.CharField(max_length=120)
    head2=models.CharField(max_length=120)
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.BigIntegerField(blank=False)
    messege=models.TextField(blank=False)
    def __str__(self):
        return self.name


class theatre(models.Model):
    para1=models.TextField()
    para2=models.TextField()
    para3=models.TextField()
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    head1=models.CharField(max_length=120)
    head2=models.CharField(max_length=120)
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.BigIntegerField(blank=False)
    messege=models.TextField(blank=False)
    def __str__(self):
        return self.name

class ACM(models.Model):
    para1=models.TextField()
    para2=models.TextField()
    para3=models.TextField()
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    head1=models.CharField(max_length=120)
    head2=models.CharField(max_length=120)
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.BigIntegerField(blank=False)
    messege=models.TextField(blank=False)
    def __str__(self):
        return self.name

class IEEE(models.Model):
    para1=models.TextField()
    para2=models.TextField()
    para3=models.TextField()
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    head1=models.CharField(max_length=120)
    head2=models.CharField(max_length=120)
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.BigIntegerField(blank=False)
    messege=models.TextField(blank=False)
    def __str__(self):
        return self.name
class contact(models.Model):
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.BigIntegerField(blank=False)
    messege=models.TextField(blank=False)
    def __str__(self):
        return self.name
