from django.contrib import admin
from .models import NewPost

@admin.register(NewPost)
class NewPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'image', 'title', 'content', 'expires', 'status')
    search_fields = ('title', 'content')
    list_filter = ('status', 'date', 'expires')
