from django.db import models
from django.db.models.base import ModelState

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    desc =  models.TextField(blank=True,null=True)
    author = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
