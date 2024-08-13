from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
  path('home/',home),
  path('add-blog/',add_blog),
  path('view-blog/',view_blog),
  path("update/<int:pk>/",update),
  path("delete/<int:pk>/",delete),
]
