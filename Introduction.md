# Full-stack-Django

### Basic Django tutorial for personal use

To run server use python manage.py runserver

For url mapping use urls.py.
Example of mapping inside urlpatterns:

````path('', views.index, name='index')````

You can also use regular expressions to map urls. Another useful thing is to link to urls.py of the corresponding apps.

````re_path(r'^first_app/', include('first_app.urls'))````

#### Templates

For templates, you should create templates folder and additional folder in the template folder for each app.

Set templates directory in ````settings.py````. Best use of pathlib (e.g. `````Path(__file__).parent.parent/"templates"`````) for universal use.

Example from views.py:
By adding a template tag into your html file you can make your site dynamic.
(``````{{insert_me}}``````)

`````
def index(request):
    dict = {'insert_me':"Hello I am from views.py"}
    return render(request, 'index.html', context = dict)
`````
In the resulting html site the corresponding dictionary value will be displayed.