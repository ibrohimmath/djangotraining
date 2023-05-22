from django.db import models
from django.contrib.auth.models import User

from typing import Union
from googletrans import Translator, constants 
from pprint import pprint 
translator = Translator()
# translation = translator.translate("salom", dest = 'ru')
# print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


class Location(models.Model):
    position = models.CharField(max_length = 100)
    def __str__(self):
        return self.position 

class Category(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name 


class Post(models.Model):
    description = models.CharField(max_length = 300)
    image = models.ImageField(upload_to = 'post_image/')
    content = models.TextField()


    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'connect')
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    reading_time = models.IntegerField(default = 0, editable = False)
    is_active = models.BooleanField(default = False)
    is_advertising = models.BooleanField(default = False)
    views_count = models.IntegerField(default = 0, editable = False)
    
    created_at = models.DateTimeField(auto_now_add = True)


        
#tillar ham qo'shilsin

    def __str__(self):
        print(self.tillar)
        return self.description.split()[0]


    def save(self):
        self.reading_time = len(self.content.split()) // 200
        super().save()



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    name = models.CharField(max_length = 256)
    email = models.EmailField()

