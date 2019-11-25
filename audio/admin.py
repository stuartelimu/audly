from django.contrib import admin

from .models import Music

class MusicAdmin(admin.ModelAdmin):
    list_display = ('title','upload', 'uploaded_at')

admin.site.register(Music, MusicAdmin)