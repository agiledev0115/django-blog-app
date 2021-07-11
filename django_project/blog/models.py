from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# makemigration is used to create our tables on make some changes to our database

# create a class for post

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # when user delete the post, then post will be deleted

    # create a dander method for how you want to printed out post
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})  # return the path of specific post, as a string