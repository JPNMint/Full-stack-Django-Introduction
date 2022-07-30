from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    dict = {'insert_me':"Hello I am from views.py, through templates/first_app/index.html"}
    return render(request, 'first_app/index.html', context = dict)

def testing(request):
    return HttpResponse("Testing urls!")
