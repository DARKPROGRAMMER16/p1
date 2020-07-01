from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    num = models.IntegerField()
    title = models.CharField(max_length = 255)
    # content = models.TextField()
    content = RichTextUploadingField(blank=True,null=True)
    # overview = models.TextField()
    overview = RichTextField(blank=True,null=True)
    # about = RichTextField(blank=True,null=True)
    about = RichTextUploadingField(blank=True,null=True)
    # about = HTMLField(blank=True,null=True)

    author = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='blog/images',default="")
    slug = models.CharField(max_length = 255)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + " - " + self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + " by "+self.user.username
    
