from django.contrib import admin

from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "category",
        "created",
        "published",
        "status",
    ]
    list_filter = ["title", "author", "category", "published", "status"]
    search_fields = ["title", "status", "published", "category__title", "created"]
    ordering = ["title", "author", "published", "status"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "id"]
    search_fields = ["title"]


admin.site.register(Post, PostAdmin)

admin.site.register(Category, CategoryAdmin)

# Register your models here.
