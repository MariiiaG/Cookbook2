from django.contrib import admin
from .models import Author, Recipe, Category
from django.utils.html import format_html


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    fields = ['last_name', 'first_name']


admin.site.register(Author, AuthorAdmin)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'display_author', 'show_photo')
    list_filter = ('category', 'author')
    readonly_fields = ['show_photo']
    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height: 100px;>')
    show_photo.short_description = 'Photo'


admin.site.register(Category)


