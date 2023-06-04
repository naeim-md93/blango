from django.contrib import admin
from .models import Tag, Post


admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    exclude = ['slug']
    list_display = ['title', 'published_at']


admin.site.register(Post, PostAdmin)
