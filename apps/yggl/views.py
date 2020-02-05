from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DayArchiveView
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger, EmptyPage

from .models import Yg, YgCategory, Bm, YgTag
# from .forms import ArticleForm, BookNotesForm


class YgListView(View):
    def get(self, request):
        # categories = BookCategory.objects.all()
        # alltags = BookTag.objects.all()
        # freqtags = alltags[0:12]
        # moretags = [tag for tag in alltags if tag not in freqtags]
        # epoches = Epoch.objects.all()
        # languages = LanguageKind.objects.all()

        # 所有员工
        yg_list = Yg.objects.all()
        # 按种类过滤
        ctg = request.GET.get('ctg', '')
        if ctg:
            yg_list = yg_list.filter(category_id=int(ctg))
        # 按部门过滤
        m = request.GET.get('m', '')
        if m:
            yg_list = yg_list.filter(bm_id=int(m))

        # 按标签过滤
        tag = request.GET.get('tag', '')
        if tag:
            yg_list = yg_list.filter(tags=tag)

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        except EmptyPage:
            page = 1

        # Provide Paginator with the request object for complete querystring generation
        paginator = Paginator(yg_list, per_page=4, request=request)

        page_obj = paginator.page(page)

        # return render(request, 'books/book_list.html', {
        #     'page_obj': page_obj,
        #     'freqtags': freqtags, 'moretags': moretags,
        #     'epoches': epoches, 'languages': languages,
        #     'lang': lang, 'epch': epch, 'ctg': ctg, 'tag': tag
        # })
        return render(request, 'yggl/yg_list.html', {
            'page_obj': page_obj, 'm': m,  'ctg': ctg, 'tag': tag
        })


class YgDetailView(View):
    def get(self, request, pk):
        yg = Yg.objects.prefetch_related('tags',).select_related(
            'category', 'bm').filter(pk=pk).first()

        return render(request, "yggl/jianli.html", {'yg':yg})


