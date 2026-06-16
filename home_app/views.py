from django.shortcuts import render
from blog_app.models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, "home_app/index.html", {'posts': posts})