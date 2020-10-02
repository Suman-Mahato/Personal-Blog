from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('blogpost/<int:id>', views.blogPost, name='blogPost'),

]