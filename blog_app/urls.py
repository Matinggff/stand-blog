from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('detail/<slug:slug>', views.post_detail, name='detail'),
    path('list', views.post_list, name='post_list'),
    path('category/<slug:slug>', views.category_detail, name='category_detail'),
    path('search', views.search, name='search'),
]