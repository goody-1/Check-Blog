from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Category(models.Model):

    ''' Post Category '''

    title = models.CharField(max_length = 200)
    # posts = models.ForeignKey(Post.title, null = True, blank = True)
    
    def posts(self):
        if Post.category == self.title:
            return Post.title

    def __str__(self):
        return self.title


class Post(models.Model):
    """ Post class """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True, blank = True)
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True, help_text = 'optional')


    def publish(self):
        ''' Assigning date to published_date '''

        self.published_date = timezone.now()
        self.save

    def __str__(self):

        ''' Name to show on admin '''

        return self.title


