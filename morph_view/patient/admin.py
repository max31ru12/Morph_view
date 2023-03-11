from django.contrib import admin
from .models import *
# Register your models here.


class MainPageVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'video_path', 'is_published')
    list_editable = ('is_published',)


admin.site.register(MainPageVideo, MainPageVideoAdmin)
