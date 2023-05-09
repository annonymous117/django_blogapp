from django.db import models

# Create your models here.
class PostContent(models.Model):
    title=models.CharField("Topic title",max_length=200)
    author=models.CharField(" Content Author",max_length=200)
    content=models.TextField(" Content ",max_length=1000)
    image=models.ImageField("Add Topic Image",upload_to="blogimages")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)