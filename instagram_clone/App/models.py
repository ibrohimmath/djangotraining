from django.db import models 
from django.contrib.auth.models import User 


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    followers = models.ManyToManyField(User, related_name = 'followers', blank = True)
    following = models.ManyToManyField(User, related_name = 'following', blank = True)
    profile_picture = models.ImageField(upload_to = 'profilepics')
    
    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'posts')
    likes = models.ManyToManyField(User, related_name = 'likes', blank = True)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)


class Reels(models.Model):
    reel = models.FileField(upload_to = 'reel')
    likes = models.ManyToManyField(User,blank = True)

class Story(models.Model):
    story = models.ImageField(upload_to = 'story')
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    