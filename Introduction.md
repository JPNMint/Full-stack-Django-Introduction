# Full-stack-Django

### Basic Django tutorial for personal use

To run server use python manage.py runserver

To create Django project `django-admin startproject first_project`

To create Django app `python manage.py startapp first_app`

For url mapping use urls.py.
Example of mapping inside urlpatterns:

`path('', views.index, name='index')`

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

Similar things can also be done for media files. For this create ````static```` folder and input mediafiles there.
Directory should be specified in the settings.py of the project.
Call `````{% load static %}````` in the html file and call static file using ````"{% static "images/football.jpg" %}"````.

#### Use of Databases

Django comes with SQLite, other engines can also be used. 
Creating database in models.py. 

```
class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length = 264, unique = True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
```

Deploy:
```
BASH
python manage.py migrate

python manage.py makemigrations app_1

python manage.py migrate
```
Now the databases should be deployed.
To confirm, you can create test data in shell.

``python manage.py shell``

This opens a python console.

Print all objects in the table.

```
from app_1.models import Topic

print(Topic.objects.all())  
```
Add object to table.

```
t = Topic(top_name = "Social Network") 
t.save()

##quit()
```

You can also use the admin interface which is much more convinient.

Edit admin.py, import and add the models.

``admin.site.register(Webpage)
``

To access admin interface, you need a superuser.

```
Bash

python manage.py createsuperuser
```

Access admin interface on browser by adding /admin.
