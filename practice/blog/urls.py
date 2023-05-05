from django.urls import path 
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', post_list, name = 'posts'),
    #path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name = 'post'),
]