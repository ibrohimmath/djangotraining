from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from post.models import Post


class IndexView(ListView):
    model = Post
    context_object_name = 'post_list'
    queryset = Post.objects.all()
    template_name = 'list.html'
    paginate_by = 2

class PostView(DetailView):
    model = Post 
    context_object_name = 'post'
    template_name = 'detail.html'
