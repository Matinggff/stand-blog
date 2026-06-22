from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/posts')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            unique_slug = slug
            counter = 1

            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{slug}-{counter}"
                counter += 1

            self.slug = unique_slug

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_app:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} | {self.created_at}"
