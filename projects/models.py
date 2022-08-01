from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=150)
    Description = models.TextField()
    gh_link = models.CharField()
    live_link = models.CharField()
    tag = models.CharField(max_length=150)
    image = models.ImageField()

    def __str__(self):
        return self.title