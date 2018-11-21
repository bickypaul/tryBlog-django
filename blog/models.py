from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from PIL import Image


# BlogPost model
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    blog_image = models.ImageField(default='default_blog_image.png', upload_to='blog_pictures')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
