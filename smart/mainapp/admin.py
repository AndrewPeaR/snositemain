from django.contrib import admin
from .models import Article, Magazine, Email, Category

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Magazine)
admin.site.register(Email)
