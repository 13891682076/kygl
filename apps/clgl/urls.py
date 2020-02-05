# -*- coding: utf-8 -*-
__author__ = 'bobby'

from django.urls import path, include

from .views import ClglView, BusDetailView, JsyDetailView

app_name = 'clgl'
urlpatterns = [
    #车辆管理
    path('clgl_index', ClglView.as_view(), name="clgl_index"),

    path("bus/<int:pk>/", BusDetailView.as_view(), name="bus"),
    path("jsy/<int:pk>/", JsyDetailView.as_view(), name="jsy"),

]