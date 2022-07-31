from django.contrib import admin
from django.urls import path, re_path
from app_1 import views

urlpatterns = [
    re_path(r'^$',views.index, name = 'index'),
    path('testpath',views.index, name = 'index'),

]
