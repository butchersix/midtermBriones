from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_updated = models.DateTimeField('date updated', auto_now_add=True)
    content = models.TextField()
    is_active = models.BooleanField(default=True)

class Comment(models.Model):
    date_created = models.DateTimeField('date created', auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
