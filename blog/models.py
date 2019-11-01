from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.SlugField()
    body = models.TextField()
    author = models.CharField(default='Hristo Todorov', max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:150]
