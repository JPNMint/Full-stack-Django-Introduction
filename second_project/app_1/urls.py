from django.contrib import admin
from django.urls import path, re_path
from app_1 import views

app_name = "app_1_tag"
urlpatterns = [
    path('',views.index, name = 'index'),
    path('model_form', views.WebpageInput, name = 'webpageinput')

]
