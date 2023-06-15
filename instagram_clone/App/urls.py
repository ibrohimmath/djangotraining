from django.urls import path 
from App import views 

urlpatterns = [
    path('', views.index, name = "index"),
    path('createprofile/', views.create_profile, name = "signup"),
    path('login/', views.Login, name = "Login"),
    path('profile/', views.profile, name = "profile"),
    path('logout/', views.Logout, name = "Logout"),
    path('search/', views.search, name = 'search'),
    path('follow/<int:id>/<str:username>/', views.follow, name = 'follow'),
    path('uploadpost/', views.upload_post, name = 'upload_post'),
    path('like/<int:id>/', views.like_post, name = 'like'),
    path('upload_reel/', views.upload_reel, name = 'upload_reel'),
    path('reels/', views.reels, name = 'reels'),
    path('uploadstory/', views.upload_story, name = 'upload_story'),
]