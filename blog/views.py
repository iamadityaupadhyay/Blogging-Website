from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from .models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,"navigation.html")

@login_required(login_url='/blog/login-page/')
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
@login_required(login_url='/blog/login-page/')
def view_blog(request):
    data=Blog.objects.all()
    context={
        "blogs":data
    }
    return render(request,"view_blog.html",context)
@login_required(login_url='/blog/login-page/')
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
from django.contrib import messages
def register(request):
    if request.method =="POST":
        data = request.POST
        first_name =data.get('first_name')
        last_name=data.get('last_name')
        username =data.get('username')
        password=data.get('password')
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username is already taken")
            return redirect("/blog/register/")
            
        
        user =User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        return redirect("/blog/login-page/")
    return render(request,"register.html")
from django.contrib.auth import authenticate
def login_page(request):
    if request.method =="POST":
        data = request.POST
        username =data.get("username")
        password=data.get('password')
        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("/blog/add-blog/")
        
        return redirect("/blog/register/")
    return render(request,"login.html")
def logout_page(request):
    logout(request)
    return redirect("/blog/login-page/")