from django.contrib import admin
from .models import Publication
# Register your models here.

@admin.register
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title','slug','content','created']
    list_filter = ['created']

@admin.register
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','publication','created')
    list_filter = ('created','updated')
    search_fields = ('user','body')