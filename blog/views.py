from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PostForm

from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    print(posts.query)
    return render(request, 'blog/blog_list.html', {'posts': posts})


def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post creado con éxito')
            return redirect('post_list')
        messages.error(request, 'Hay errores en el formulario')
    return render(request, 'blog/blog_create.html', {'form': form})


def post_update(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'blog/blog_update.html', {'form': form, 'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('post_list')
