

from datetime import datetime
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200,null=False,blank=False)
    content=models.TextField(blank=False,null=False)
    image=models.ImageField(blank=True,null=True,upload_to='postimage/')
    create=models.DateField(auto_now_add=True)

        
    def __str__(self):
        return self.title
    
    
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="User_image", blank=True,null=True, default='default.png')
    bio=models.CharField(max_length=400,null=True,blank=True ,default="Bio Empty..!!")
    about=models.TextField(blank=True,null=True,  default="About Empty..!!")
    def __str__(self):
        return self.user.username
class Background(models.Model):
    image=models.ImageField(upload_to="bg_image", blank=False,null=False)
    title=models.CharField(max_length=300,null=False,blank=False)
    def __str__(self):
        return self.title
    
    