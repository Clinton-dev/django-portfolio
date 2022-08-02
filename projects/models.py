from django.db import models
from cloudinary.models import CloudinaryField


class Project(models.Model):
    title = models.CharField(max_length=150)
    Description = models.TextField()
    gh_link = models.CharField(max_length=200)
    live_link = models.CharField(max_length=200)
    tag = models.CharField(max_length=150)
    # image = models.ImageField()
    image = CloudinaryField('image')
    category = models.CharField(max_length=150)


    def __str__(self):
        return self.title