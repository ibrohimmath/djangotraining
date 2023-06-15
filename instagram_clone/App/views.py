from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from App.models import Profile, Post, Reels, Story

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.db.models import Q 

def index(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    posts = Post.objects.filter(Q(profile__followers = request.user))
    # posts = Post.objects.filter(Q(profile__followers = request.user) & ~Q(likes = request.user))
    story = Story.objects.filter(profile__followers = request.user)
    context = {'posts': posts, 'stories': story}
    return render(request, 'index.html', context)

def Login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('profile')
    return render(request, 'Login.html')


def create_profile(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        image = request.FILES['image']
        user = User.objects.create_user(username = username, password = password)
        profile = Profile.objects.create(user = user, profile_picture = image)
        if profile:
            messages.success(request, 'Profile created, please Login')
            return redirect("Login")
    return render(request, 'SignUp.html')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(user = request.user)
    posts_num = posts.count()
    return render(request, 'profile.html', {'profile': profile, 'profile_of_user': True, 'posts': posts, 'posts_num': posts_num})


def Logout(request):
    logout(request)
    return redirect('Login')


def search(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    search = request.GET.get('username', False)
    profiles = Profile.objects.filter(user__username__icontains = search)
    context = {'profiles': profiles, 'username': search}
    return render(request, 'search.html', context)

def follow(request, id, username):
    profile = Profile.objects.get(id = id)
    login_profile = Profile.objects.get(user = request.user)
    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
        login_profile.following.remove(profile.user)
    else:
        profile.followers.add(request.user)
        login_profile.following.add(profile.user)
    return redirect(f'/search/?username = {username}')


def upload_post(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    if request.method == 'POST':
        post = request.FILES['post']
        profile = Profile.objects.get(user = request.user)
        posts = Post.objects.create(user = request.user, image = post, profile = profile)
        if posts:
            messages.success(request, 'POST uploaded')
    return render(request, 'uploadposts.html')

# def like_post(request, id):
#     post = Post.objects.filter(id = id)
#     return HttpResponse(post.count())

def like_post(request, id):
    post = Post.objects.filter(id = id)[0]
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('index')


def upload_reel(request):
    if not request.user.is_authenticated:
        return redirect('Login')

    if request.method == 'POST':
        reel = request.FILES['reel']
        reels = Reels.objects.create(reel = reel)
        if reels:
            messages.success(request, 'REEL UPLOADED')
    return render(request, 'uploadreels.html')


# For exploring reels
def reels(request): 
    reels = Reels.objects.all()
    return render(request, 'reels.html', {'reels': reels})

def upload_story(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    if request.method == 'POST':
        story = request.FILES['story']
        profile = Profile.objects.get(user = request.user)
        story_upload = Story.objects.create(story = story, profile = profile)
        if story_upload:
            messages.success(request, 'STORY UPLOADED')
    return render(request, 'uploadStory.html')