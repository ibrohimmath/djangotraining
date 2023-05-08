from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
 
def post_list(request):
    object_list = Post.published.all()
    num = len(object_list)
    if num < 2: side_objects = object_list        
    else: side_objects = object_list[:2]
    dic = {}
    for element in side_objects:
        dic[element.title] = [element.get_absolute_url, ]
        if len(element.body) < 30:
            dic[element.title].append(element.body + '...')
        else:
            dic[element.title].append(element.body[:30] + '...')
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts, 'dic': dic})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug = post,
    status = 'published',
    publish__year = year,
    publish__month = month,
    publish__day = day)
    return render(request, 'blog/post/detail.html', {'post': post} )