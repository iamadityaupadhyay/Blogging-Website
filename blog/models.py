from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_name=models.CharField(max_length=200,null=True,blank =True)
    blog_description=models.CharField(max_length=200,null=True,blank =True)
    blog_image=models.ImageField(upload_to="blog_images/")
