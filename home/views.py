from django.shortcuts import render
from blog.models import Post
from blog.views import post_detail

# Create your views here.



def index(request):
    post = Post.objects.last()
    post1 = {'Post': post 
    }
    return render(request, 'home/index.html', post1)

