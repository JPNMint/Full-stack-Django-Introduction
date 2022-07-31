from django.shortcuts import render

# Create your views here.
def index(request):
    dict={"insert_content":"Hello from app_1"}
    return render(request, 'app_1/index.html', context = dict)