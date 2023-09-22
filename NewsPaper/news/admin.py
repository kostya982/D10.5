from django.contrib import admin
from .models import Comment, PostCategory, Post, Category, Author

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Author)
