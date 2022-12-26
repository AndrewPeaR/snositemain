from django.contrib import admin
from django.urls import path
# from django.urls import re_path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    # path('search/', search, name='search'),
    # path('search/<str:search_str>/', search),
    path('articles', articles, name="articles"),
    path('articles/<str:filter>/', articles),
    path('archive', archive, name='archive'),
    path('for_authors', for_authors, name='for_authors'),
    path('article/<int:id>', article, name='article'),
    path('archive', archive, name='archive'),
    path('send_article', send_article, name='send_article'),
    path('about', about, name='about'),
]