from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=12000)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse('article', args=(str(self.pk)))
