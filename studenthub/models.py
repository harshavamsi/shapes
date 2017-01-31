from __future__ import unicode_literals

from django.db import models
import os
from django.utils.crypto import get_random_string
def update_image_name(instance,filename):
    path = 'heads/'
    fmt = get_random_string() + "." + filename.split('.')[-1]
    return os.path.join(path,fmt)

class dance(models.Model):
    para1=models.TextField(blank=True)
    para2=models.TextField(blank=True)
    para3=models.TextField(blank=True)
    image1 = models.ImageField(blank=True, upload_to=update_image_name)
    image2 = models.ImageField(blank=True, upload_to=update_image_name)
    head1=models.CharField(max_length=120,blank=True)
    head2=models.CharField(max_length=120,blank=True)
    web=models.CharField(max_length=120,blank=True)
    def __str__(self):
        return self.head1

class music(models.Model):
    para1=models.TextField(blank=True)
    para2=models.TextField(blank=True)
    para3=models.TextField(blank=True)
    image1 = models.ImageField(blank=True, upload_to=update_image_name)
    image2 = models.ImageField(blank=True, upload_to=update_image_name)
    head1=models.CharField(max_length=120,blank=True)
    head2=models.CharField(max_length=120,blank=True)
    web=models.CharField(max_length=120,blank=True)
    def __str__(self):
        return self.head1


class quiz(models.Model):
    para1=models.TextField(blank=True)
    para2=models.TextField(blank=True)
    para3=models.TextField(blank=True)
    image1 = models.ImageField(blank=True, upload_to=update_image_name)
    image2 = models.ImageField(blank=True, upload_to=update_image_name)
    head1=models.CharField(max_length=120,blank=True)
    head2=models.CharField(max_length=120,blank=True)
    web=models.CharField(max_length=120,blank=True)
    def __str__(self):
        return self.head1


class sankalp(models.Model):
    para1=models.TextField(blank=True)
    para2=models.TextField(blank=True)
    para3=models.TextField(blank=True)
    image1 = models.ImageField(blank=True, upload_to=update_image_name)
    image2 = models.ImageField(blank=True, upload_to=update_image_name)
    head1=models.CharField(max_length=120,blank=True)
    head2=models.CharField(max_length=120,blank=True)
    web=models.CharField(max_length=120,blank=True)
    def __str__(self):
        return self.head1

class theatre(models.Model):
    para1=models.TextField(blank=True)
    para2=models.TextField(blank=True)
    para3=models.TextField(blank=True)
    image1 = models.ImageField(blank=True, upload_to=update_image_name)
    image2 = models.ImageField(blank=True, upload_to=update_image_name)
    head1=models.CharField(max_length=120,blank=True)
    head2=models.CharField(max_length=120,blank=True)
    web=models.CharField(max_length=120,blank=True)
    def __str__(self):
        return self.head1

class acm(models.Model):
    para1=models.TextField(blank=True)
    para2=models.TextField(blank=True)
    para3=models.TextField(blank=True)
    image1 = models.ImageField(blank=True, upload_to=update_image_name)
    image2 = models.ImageField(blank=True, upload_to=update_image_name)
    head1=models.CharField(max_length=120,blank=True)
    head2=models.CharField(max_length=120,blank=True)
    web=models.CharField(max_length=120,blank=True)
    def __str__(self):
        return self.head1

class ieee(models.Model):
    para1=models.TextField(blank=True)
    para2=models.TextField(blank=True)
    para3=models.TextField(blank=True)
    image1 = models.ImageField(blank=True, upload_to=update_image_name)
    image2 = models.ImageField(blank=True, upload_to=update_image_name)
    head1=models.CharField(max_length=120,blank=True)
    head2=models.CharField(max_length=120,blank=True)
    web=models.CharField(max_length=120,blank=True)
    def __str__(self):
        return self.head1

class Contact(models.Model):
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.TextField(blank=False)
    message=models.TextField(blank=False)
    def __str__(self):
        return self.name

class musicContact(models.Model):
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.BigIntegerField(blank=False)
    message=models.TextField(blank=False)
    def __str__(self):
        return self.name

class danceContact(models.Model):
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.TextField(blank=False)
    message=models.TextField(blank=False)

    def __str__(self):
        return self.name
class quizContact(models.Model):
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.TextField(blank=False)
    message=models.TextField(blank=False)

    def __str__(self):
        return self.name

class sankalpContact(models.Model):
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.TextField(blank=False)
    message=models.TextField(blank=False)

    def __str__(self):
        return self.name

class theatreContact(models.Model):
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.TextField(blank=False)
    message=models.TextField(blank=False)

    def __str__(self):
        return self.name


class acmContact(models.Model):
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.TextField(blank=False)
    message=models.TextField(blank=False)

    def __str__(self):
        return self.name

class ieeeContact(models.Model):
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=125,blank=False)
    phone=models.TextField(blank=False)
    message=models.TextField(blank=False)
    
    def __str__(self):
        return self.name
