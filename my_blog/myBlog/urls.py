from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='myBlog-home'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # expects app/model_viewtype.html
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # expects app/model_form.html
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # expects a confirmation form
    path('about/', views.about, name='myBlog-about'),
]


