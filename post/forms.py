from django.forms import ModelForm
from .models import Post, Comment

class PostModelForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['id', 'date_created', 'date_updated', 'is_active']

class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['id', 'date_created', 'post']