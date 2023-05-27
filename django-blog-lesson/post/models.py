from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=256)
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    content = models.TextField()

    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_category_names(self):
        categories = self.category.all().values_list('title', flat = True)
        return ' . '.join(categories)
    
    def get_absolute_url(self):
        return reverse('post-detail', args = str(self.id))

class Comment(models.Model):
    text = models.TextField()

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text