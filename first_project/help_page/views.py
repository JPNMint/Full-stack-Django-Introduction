from django.shortcuts import render

# Create your views here.

def help_index(request):
    dict = {'helping':"Using templates is cool",'Another_help':'Another one'}
    return render(request, 'help_page/help.html', context = dict)
