from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostModelForm, CommentModelForm

# Create your views here.
def index(request):
    # return HttpResponse('Hello World!')
    context = {}
    posts = Post.objects.all().order_by('-date_created')
    context['posts'] = posts
    return render(request, 'index.html', context)

def help(request):
    return HttpResponse('This is a help page.')

def detail(request, post_id):
    context = {}
    context['posts'] = Post.objects.get(id=post_id)
    return render(request, 'details.html', context)

def update(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post:details', post_id)
        else:
            context['form'] = form
            render(request, 'updatepost.html', context)
    else:
        context['form'] = PostModelForm(instance=post)
    return render(request, 'updatepost.html', context)

def createPost(request):
    context = {}
    form = PostModelForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('post:index')
        else:
            context['form'] = form
            return render(request, 'createpost.html', context)
    else:
        context['form'] = form
    return render(request, 'createpost.html', context)

def createComment(request, post_id):
    context = {}
    form = CommentModelForm(request.POST)
    context['post_id'] = post_id
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save()
            comment.post = Post.objects.get(id=post_id)
            comment.save()
            return redirect('post:details', post_id)
        else:
            context['form'] = form
            return render(request, 'createcomment.html', context)
    else:
        context['form'] = form
    return render(request, 'createcomment.html', context)