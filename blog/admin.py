from django.contrib import admin
from .models import Post, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_date']

reg = admin.site.register

reg(Post, PostAdmin)
reg(Category)