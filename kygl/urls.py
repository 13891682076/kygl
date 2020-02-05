"""kygl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin
from kygl.settings import MEDIA_ROOT

urlpatterns = [
    # 后台管理系统
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # DjangoUeditor的urls
    re_path(r'^ueditor/', include('DjangoUeditor.urls')),
    # CKEditor的url
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # 评论相关的URL
    re_path(r'mpttcomments', include('django_mptt_comments.urls')),
    re_path(r'captcha', include('captcha.urls')),
    # 多媒体文件的url
    # 配置上传文件的访问处理函数
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # 第三方 账号管理
    path("accounts/", include("allauth.urls")),
    # 用户管理
    path("users/", include("users.urls", namespace="users")),
    # 员工管理
    path("yggl/", include("yggl.urls", namespace="yggl")),
    # 车辆管理
    path("clgl/", include("clgl.urls", namespace="clgl")),
    # 新闻管理
    path("news/", include("news.urls", namespace="news")),

    # 主页
    path("", TemplateView.as_view(template_name='home.html'), name='home')
]
