from django.shortcuts import render
from app_1.models import Topic, Webpage, AccessRecord
from . import forms

# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.all()
        #.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'app_1/index.html', context = date_dict)
    #return render(request, 'testing.html', locals())





def form_name_view(request):
    form = forms.FormName()
    return render(request, 'app_1/form_page.html', {'form':form})