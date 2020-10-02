from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('post', views.post, name='post'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
]