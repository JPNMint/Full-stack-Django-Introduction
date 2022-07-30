# Full-stack-Django

### Basic Django tutorial for personal use

To run server use python manage.py runserver

For url mapping use urls.py.
Example of mapping inside urlpatterns:

````path('', views.index, name='index')````

You can also use regular expressions to map urls. Another useful thing is to link to urls.py of the corresponding apps.

````re_path(r'^first_app/', include('first_app.urls'))````


For templates, you should create templates folder and additional folder in the template folder for each app.



