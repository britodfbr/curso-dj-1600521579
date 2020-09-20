from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'title', 'slug', 'author', 'published', 'created', 'changed', 'status',
    search_fields = 'title', 'content',


