from django.db import models

class News(models.Model):
    title = models.CharField(max_length=350)
    author = models.CharField(max_length=50)
    points = models.IntegerField()
    comments = models.IntegerField()
    link = models.URLField()

    def __str__(self) -> str:
        return self.title