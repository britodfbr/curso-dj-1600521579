from django.contrib import admin

# Register your models here.
from .models import Post, Category


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = 'name', 'published', 'created',
    list_filter = 'name', 'published', 'created',
    date_hierarchy = 'published'
    search_fields = 'name',


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'title', 'slug', 'author', 'published', 'created', 'changed', 'status',
    list_filter = 'slug', 'author', 'published', 'created', 'changed', 'status',
    search_fields = 'title', 'content',
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published'
    raw_id_fields = 'author',


if __name__ == '__main__':
    pass
    """
    from django.contrib.auth.models import User
    user = User.objects.get(username='admin')
    p = 'Testando o shell do Django'
    post = Post(title=p, slug=p.lower().replace(' ', '_'), content=p.upper(), author=user)
    frase = 'Criado via bulk {}'
    posts = [Post(title=frase.format(x), slug=frase.format(x).lower().replace(' ', '_'),
                  content=frase.format(x).upper(), author=user)
             for x in range(10)]
    Post.objects.bulk_create(posts)
    """
