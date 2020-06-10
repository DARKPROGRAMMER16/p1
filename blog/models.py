from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    num = models.IntegerField()
    title = models.CharField(max_length = 255)
    content = models.TextField()
    overview = models.TextField()
    author = models.CharField(max_length = 255)
    slug = models.CharField(max_length = 255)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + " - " + self.author

