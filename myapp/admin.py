from django.contrib import admin
from .models import Events, Blog, Post, Comment, Category, Author, PostView, Upload

# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(PostView)
admin.site.register(Upload)