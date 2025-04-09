from django.contrib import admin
from .models import *

admin.site.register(Live_index)
admin.site.register(Contact)
admin.site.register(history)
@admin.register(Articel)
class ArticelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'article', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('name', 'email', 'message')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
