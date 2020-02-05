from django.urls import path
from django.views.generic import ArchiveIndexView

from .models import Yg
from .views import YgListView, YgDetailView
app_name = "yggl"

urlpatterns = [
    path('list/', YgListView.as_view(), name='yg_list'),
    path('yg/<int:pk>/', YgDetailView.as_view(), name='yg_detail'),

]
