from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null =True,blank =True)
    blog_name=models.CharField(max_length=200,null=True,blank =True)
    blog_description=models.CharField(max_length=200,null=True,blank =True)
    blog_image=models.ImageField(upload_to="blog_images/")
