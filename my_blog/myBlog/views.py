from django.shortcuts import render, get_object_or_404

from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'myBlog/home.html', context)


# class based views offer built in functionality to handle common nuances of websites
class PostListView(ListView):
    model = Post
    template_name = 'myBlog/home.html'  # app/model_viewtype.html
    context_object_name = 'posts' 
    ordering = ['-date_posted']
    paginate_by = 6

class UserPostListView(ListView):
    model = Post
    template_name = 'myBlog/user_posts.html'  # app/model_viewtype.html
    context_object_name = 'posts' 
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        # set the author to the current user
        if self.request.user :
            form.instance.author = self.request.user
            return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        # set the author to the current user
        if self.request.user :
            form.instance.author = self.request.user
            return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    
    # if successfully deleted, it redirects to the home page
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'myBlog/about.html', {'title' : 'About'})
