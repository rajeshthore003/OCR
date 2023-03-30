from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.TextField()
    age  = models.IntegerField()
    img  = models.ImageField(upload_to='pics') #Pics is the folder Where we want to upload the image