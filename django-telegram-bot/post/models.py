from django.db import models 
from django.contrib.auth.models import User 

class Post(models.Model):
    description = models.CharField(max_length = 64)
    text = models.CharField(max_length = 256)
    image = models.ImageField(upload_to = 'images/')
    author = models.ManyToManyField(User)
    def __str__(self):
        return str(self.description)

class Profile(models.Model):
    name = models.CharField(max_length = 128)
    surname = models.CharField(max_length = 128)
    image = models.ImageField(upload_to = 'images/')
    # video = models.FileField(upload_to = 'videos/')        
    
