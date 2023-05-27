# urls.py
from django.urls import path
from post.views import IndexView, PostView


urlpatterns = [
    path("", IndexView.as_view(), name = 'post-detail'),
    path("post/<int:id>/", PostView.as_view(), name = 'one_post')
]
