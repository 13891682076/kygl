from django.contrib import admin

from .models import Yg, YgCategory, Bm, YgTag


class YgglAdmin(admin.ModelAdmin):
    fieldsets = [
        ('分类字段', {'fields': ['category', 'epoch', 'languagekind', 'tags', 'degree', 'recommend']}),
        ('出版字段', {'fields': ['publisher', 'author']}),
        ('内容字段', {'fields': ['title', 'abstract', 'desc', 'cover']}),
        ('统计字段', {'fields': ['wordcount', 'starnums', ]}), #'readernum', 'clicknum', 'favornum'
    ]


admin.site.register(YgCategory)
admin.site.register(YgTag)
admin.site.register(Bm)
admin.site.register(Yg)

