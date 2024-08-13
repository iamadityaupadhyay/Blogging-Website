from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    return render(request,"navigation.html")
def add_blog(request):
    if request.method =="POST":
        data = request.POST
        blog_name=data.get('blog_name')
        blog_description=data.get("blog_description")
        try:
            blog_image=request.FILES['blog_image']
        except:
            blog_image=None
        blog = Blog.objects.create(
            blog_name=blog_name,
            blog_description=blog_description,
            blog_image=blog_image
        )
        blog.save()
        return redirect("/blog/view-blog/")
    return render(request,"add_blog.html")
def view_blog(request):
    data=Blog.objects.all()
    context={
        "blogs":data
    }
    return render(request,"view_blog.html",context)
def delete(request,pk):
    queryset=Blog.objects.get(id=pk)
    queryset.delete()
    return redirect("/blog/view-blog/")
def update(request,pk):
    if request.method =="POST":
        data = request.POST
        blog_name=data.get('blog_name')
        blog_description=data.get("blog_description")
        try:
            blog_image=request.FILES['blog_image']
        except:
            blog_image=None
        blog = Blog.objects.get(id=pk)
        blog.blog_name=blog_name
        blog.blog_description=blog_description
        blog.blog_image= blog_image
        blog.save()
        return redirect("/blog/view-blog/")
    return render(request,"update.html")