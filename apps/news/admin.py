from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['uuid_id', 'user', 'reply', 'content', 'parent_id']


admin.site.register(News, NewsAdmin)
