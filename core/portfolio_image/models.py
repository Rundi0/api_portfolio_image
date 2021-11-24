from django.conf import settings
from django.db import models
from django.utils import timezone


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)


class Image(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images')
    created_date = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100, default="anonim")
    text = models.CharField(max_length=500, default=None)