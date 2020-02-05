import xadmin
from .models import Yg, YgCategory, Bm, YgTag


class YgCategoryAdmin(object):
    list_display = ['id', 'catname', 'created_at', 'updated_at']
    list_editable = ['catname', ]
    model_icon = 'fa fa-flag'


class YgTagAdmin(object):
    list_display = ['id', 'tagname', 'created_at', 'updated_at']
    list_editable = ['tagname', ]
    model_icon = 'fa fa-tag'


class BmAdmin(object):
    list_display = ['id', 'name', 'created_at', 'updated_at']
    list_editable = ['name', ]
    model_icon = 'fa fa-file-text-o'




class YgAdmin(object):
    list_display = ['id', 'category', 'bm', 'tags', 'name', 'sfz', 'sfz_img', 'gender',
                    'address', 'desc', 'mobile', 'is_zg']
    list_editable = ['id', 'category', 'bm', 'tags', 'name', 'sfz', 'sfz_img', 'gender',
                    'address', 'desc', 'mobile', 'is_zg' ]
    list_filter = ['id', 'category', 'bm', 'tags', 'name', 'sfz', 'sfz_img', 'gender',
                    'address', 'desc', 'mobile', 'is_zg',
                   'created_at', 'updated_at']
    style_fields ={'desc': 'ueditor'}
    search_fields = ['name', 'address', 'desc']
    model_icon = 'fa fa-book'
    readonly_fields = []

    refresh_times = [50, 100]




xadmin.site.register(YgCategory, YgCategoryAdmin)
xadmin.site.register(YgTag, YgTagAdmin)
xadmin.site.register(Bm, BmAdmin)
xadmin.site.register(Yg, YgAdmin)

