from django.db import models
from django.utils import timezone

# import user model
from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    # if a user is deleted the user's posts are removed
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # return the url to be redirected to after creating the post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk' : self.pk})