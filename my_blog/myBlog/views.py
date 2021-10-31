from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'myBlog/home.html', context)

def about(request):
    return render(request, 'myBlog/about.html', {'title' : 'About'})
