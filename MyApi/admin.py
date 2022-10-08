from django.contrib import admin
from .models import *


class SongList(admin.ModelAdmin):
    list_display = ['title', 'singer', 'duration']

    class Meta:
        model = Song
# Register your models here.


admin.site.register(Song, SongList)
admin.site.register(Singer)