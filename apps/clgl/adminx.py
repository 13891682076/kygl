# -*- coding: utf-8 -*-
__author__ = 'bobby'
__date__ = '2016/10/25 23:52'
import xadmin

from .models import Bus,Jsy,Spy,Bus_user


class BusAdmin(object):
    list_display = ['name', 'image','desc','xsz','yyz','rh_time','lxdj','bm']
    search_fields = ['name','desc','xsz','yyz','bm']
    list_filter = ['name', 'image','desc','xsz','yyz','rh_time','lxdj','bm']
    list_per_page = 18
    model_icon = 'fa fa-university'
    style_fields = {'desc': 'ueditor'}

class Bus_userAdmin(object):
    list_display = ['name', 'bm','sfz','gender','address','mobile','cb_time','updated_at']
    search_fields = ['name', 'bm','sfz','gender','address','mobile']
    list_filter = ['name', 'bm','sfz','gender','address','mobile']
    list_per_page = 18
    model_icon = 'fa fa-university'
    style_fields = {'detail': 'ueditor'}


class JsyAdmin(object):
    list_display = ['name', 'jsz','bm','gender', 'is_zg']
    search_fields = ['name', 'jsz','bm','gender', 'is_zg']
    list_filter = ['name', 'jsz','bm','gender', 'is_zg']
    list_per_page = 18
    model_icon = 'fa fa-university'
    style_fields = {'detail': 'ueditor'}


class SpyAdmin(object):
    list_display = ['name', 'sfz', 'bm', 'gender', 'is_zg']
    search_fields = ['name', 'sfz', 'bm', 'gender', 'is_zg']
    list_filter = ['name', 'sfz', 'bm', 'gender', 'is_zg']
    list_per_page = 18
    model_icon = 'fa fa-university'
    style_fields = {'detail': 'ueditor'}

class MyAdmin(object):
    list_display = ['title','content']
    style_fields ={'content':'ueditor'}

xadmin.site.register(Bus, BusAdmin)
xadmin.site.register(Jsy, JsyAdmin)
xadmin.site.register(Spy, SpyAdmin)
xadmin.site.register(Bus_user, Bus_userAdmin)


