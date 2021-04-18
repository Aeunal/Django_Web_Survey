from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^update/(?P<id>\d+)/$', views.update, name='update'),
    path('update_1/', views.update_1, name='update_1'),
]