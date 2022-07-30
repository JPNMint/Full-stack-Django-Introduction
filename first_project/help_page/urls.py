from django.contrib import admin
from django.urls import path, re_path
from help_page import views

from django.conf.urls import include

urlpatterns = [
    path('',views.help_index, name='helping')
]