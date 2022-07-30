from django.contrib import admin
from django.urls import path, re_path
from first_app import views

from django.conf.urls import include

urlpatterns = [
    re_path(r'^$',views.testing, name='testing')
]