from django.shortcuts import render
from app_1.models import Topic, Webpage, AccessRecord
from . import forms

from app_1.forms import NewWebpage

# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.all()
        #.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'app_1/index.html', context = date_dict)
    #return render(request, 'testing.html', locals())





def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validation success")
            print("Name: "+form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    return render(request, 'app_1/form_page.html', {'form':form})


def WebpageInput(request):
    form = NewWebpage()

    if request.method == 'POST':
        form = NewWebpage(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("Error")

    return render(request, 'app_1/model_form.html', {'modelform':form})