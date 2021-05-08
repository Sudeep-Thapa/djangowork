from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('services', service, name='services'),
    path('price', price, name='price'),
    path('portfolio', portfolio, name='portfolio'),
    path('elements', elements, name='elements'),
    path('contacts', contacts, name='contacts'),
    path('blog-single', blog_single, name='blog-single'),
    path('blog-home', blog_home, name='blog-home'),
]
