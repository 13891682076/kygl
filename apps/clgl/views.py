from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DayArchiveView
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger, EmptyPage


from .models import *


class ClglView(View):
    def get(self, request):


        # 所有车辆
        bus_list = Bus.objects.all()
        # 按种类过滤
        ctg = request.GET.get('ctg', '')
        if ctg:
            bus_list = bus_list.filter(category_id=int(ctg))
        # 按部门过滤
        m = request.GET.get('m', '')
        if m:
            bus_list = bus_list.filter(bm_id=int(m))

        # 按标签过滤
        tag = request.GET.get('tag', '')
        if tag:
            bus_list = bus_list.filter(tags=tag)

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        except EmptyPage:
            page = 1

        # Provide Paginator with the request object for complete querystring generation
        paginator = Paginator(bus_list, per_page=4, request=request)

        page_obj = paginator.page(page)

        # 所有车辆经营者
        bususer_list = Bus_user.objects.all()
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        except EmptyPage:
            page = 1

        # Provide Paginator with the request object for complete querystring generation
        paginator = Paginator(bususer_list, per_page=4, request=request)

        user_obj = paginator.page(page)
        return render(request, 'clgl/clgl_index.html', {
            'page_obj': page_obj,'user_obj':user_obj, 'm': m,  'ctg': ctg, 'tag': tag
        })
    # def index(request):
    #     return render(request,'clgl/clgl_index.html',{})
class BusListView(View):


    def get(self, request):
        # categories = BookCategory.objects.all()
        # alltags = BookTag.objects.all()
        # freqtags = alltags[0:12]
        # moretags = [tag for tag in alltags if tag not in freqtags]
        # epoches = Epoch.objects.all()
        # languages = LanguageKind.objects.all()

        # 所有车辆
        bus_list = Bus.objects.all()
        # 按种类过滤
        ctg = request.GET.get('ctg', '')
        if ctg:
            bus_list = bus_list.filter(category_id=int(ctg))
        # 按部门过滤
        m = request.GET.get('m', '')
        if m:
            bus_list = bus_list.filter(bm_id=int(m))

        # 按标签过滤
        tag = request.GET.get('tag', '')
        if tag:
            bus_list = bus_list.filter(tags=tag)

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        except EmptyPage:
            page = 1

        # Provide Paginator with the request object for complete querystring generation
        paginator = Paginator(bus_list, per_page=4, request=request)

        page_obj = paginator.page(page)

        # return render(request, 'books/book_list.html', {
        #     'page_obj': page_obj,
        #     'freqtags': freqtags, 'moretags': moretags,
        #     'epoches': epoches, 'languages': languages,
        #     'lang': lang, 'epch': epch, 'ctg': ctg, 'tag': tag
        # })
        return render(request, 'clgl/bus_list.html', {
            'page_obj': page_obj, 'm': m,  'ctg': ctg, 'tag': tag
        })


class BusDetailView(View):
    def get(self, request, pk):
        # bus = Bus.objects.prefetch_related('',).select_related( '').filter(pk=pk).first()
        bus = Bus.objects.filter(pk=pk).first()

        return render(request, "clgl/bus.html", {'bus':bus})
class JsyDetailView(View):
    def get(self, request, pk):
        # bus = Bus.objects.prefetch_related('',).select_related( '').filter(pk=pk).first()
        jsy = Jsy.objects.filter(pk=pk).first()

        return render(request, "clgl/jsy.html", {'jsy':jsy})
class SpyDetailView(View):
    def get(self, request, pk):
        # bus = Bus.objects.prefetch_related('',).select_related( '').filter(pk=pk).first()
        jsy = Spy.objects.filter(pk=pk).first()

        return render(request, "clgl/bus.html", {'spy':spy})


