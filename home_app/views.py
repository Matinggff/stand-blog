from django.shortcuts import render
from blog_app.models import Post, Category


def home(request):
    posts = Post.objects.all()
    return render(request, "home_app/index.html", {'posts': posts})


def sidebar(request):
    categories = Category.objects.all()
    return render(request, 'includes/sidebar.html', {'categories': categories})