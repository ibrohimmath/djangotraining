from django.http import HttpResponse 
from django.shortcuts import render
from blog.models import Post  

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts, })