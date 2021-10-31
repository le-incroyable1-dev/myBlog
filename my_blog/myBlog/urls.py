from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='myBlog-home'),
    path('about/', views.about, name='myBlog-about'),
]
