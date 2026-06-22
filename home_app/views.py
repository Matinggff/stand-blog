from django.shortcuts import render
from blog_app.models import Post

def home(request):
    posts = Post.objects.all()
    recent_posts = Post.objects.order_by('-updated_at')[:3]
    return render(request, "home_app/index.html", {'posts': posts, 'recent_posts': recent_posts})