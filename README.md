# Django-starter-with-models

### This basic starter for django I have gone through the steps of creating a project and app for future reference. This is a django application for saving employee information and rendering it to the webpage.

## Pre-requisites:

-   Python
-   Django

## For running the app:

```
python3 manage.py runserver
```

<br/>

# Steps for creating the same app:

## 1. Creating new site

```
➜ django-admin startproject employee_site
```

<br/>

## 2. Creating new app

```
➜ django-admin startapp employees
```

-❗️ In the whole doc I will be referring **employee_site** as **site** and **employees** as **app**

-❗️ In the shell commands I have used **python3** since I have a linux OS. If you are using windows use **python** instead of **python3**

<br/>

## 3. Creating new view

1. Add new view in **views.py** of app
2. Create **urls.py** file in "app" directory
3. Copy paste the following code in view.py

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def employees_page(request):
   return HttpResponse('Hello World')
```

4. Add the url for view in **urls.py**

```python
from django.urls import path
from .import  views
urlpatterns = [
	path('',views.employees_page, name="employees")
]
```

5. Go to **urls.py** in "site" and add new path to the app using include method.

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include("employees.urls")),
]

```

6. Now we can go the url mentioned in the app we can see the response added in **views.py**

```url
http://localhost:8000/employees/
```

<br/>

## 4. Adding models

1. Go to **models.py** in "app" and create new model:

```python
from django.db import models

# Create your models here.
class employees_db(models.Model):
	emp_id = models.AutoField
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	dept = models.CharField(max_length=30)
	salary = models.IntegerField()

	def __str__(self):
	 return self.firstName
```

2. For adding the model inside to the **site** we have to add the **appConfig** inside the **site's** **settings.py**
3. For copying the config first go to **apps.py** in "app" copy the "AppNameConfig" in our example it is **EmployeesConfig**. It wil be created automatically.

```python
from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    name = 'employees'

```

4. Now go to **settings.py** in site and go to installed apps list and add "appName.apps.AppNameConfig" in our example it is **EmployeesConfig**.

```python
INSTALLED_APPS = [
    'employees.apps.EmployeesConfig',
    'django.contrib.admin',
    ...
]
```

5. Go to terminal and update the migrations and migrate. Make sure you are in the same directory as **manage.py**

```
➜ python3 manage.py makemigrations
➜ python3 manage.py migrate
```

Now our models are added to the database.

<br/>

## 5. Accessing the admin panel

1. First we have to create a new super user

```
➜ python3 manage.py createsuperuser
```

2. Add the appropriate info and password
3. Run server and

```
➜ python3 manage.py runserver
```

4. Go to /admin page and add the admin name and password

```
http://localhost:8000/admin
```

<br/>

## 6. Registering the models

1. In order to use the models we have to register it
2. For doing that go to **admin.py** in **app**
3. Import our newly created model
4. Register the model
5. Code :

```python
from django.contrib import admin
from .models import employees_db

# Register your models here.
admin.site.register(employees_db)
```

5. Restart the server
   We can check the models filed in our admin panel now

<br/>

## 7. Creating templates and adding it to views

1. Create new folder named "templates" in app directory and add new html file

```
➜ mkdir templates
➜ touch index.html
```

2. Now go to **views.py** in our app and add return statement which renders our html page in **templates**

```
return render(request, 'index.html',dbData)
```

<br/>

## 8. Fetching the data from models

1. First go to admin page:

```
http://localhost:8000/admin
```

2. Now you can see that **employees_db** has been created we can click on it and add new employees
3. Once it is done go to **view.py** in **app**
4. Now first we will import our **model** which is **employees_db** and then store the **db data** to one variable and pass that data to the template as a third parameter.
5. Code:

```python
from django.shortcuts import render
from django.http import HttpResponse
from employees.models import employees_db

# Create your views here.
def employees_page(request):

	# fetching data from models
	dbData = {"data" : employees_db.objects.all()}

	return render(request, 'index.html',dbData)
```

6. Now we can access data from Database through **dbData** variable.

<br/>

## 9. Rendering data to templates

1. Go to **templates\/** and open **index.html**
2. We can use the **data** key passed in the **dbData** object/dictionary.
3. We loop over it and render the values of attributes for eg. **emp.firstName** will give us firstName value.

```html
<div class="container-style">
	{% for emp in data %}
	<div class="emp-card">
		<p class="id"><b>ID:</b> {{emp.id}}</p>
		<p class="name"><b>Name:</b> {{emp.firstName}} {{emp.lastName}}</p>
		<p class="dept"><b>Dept:</b> {{emp.dept}}</p>
		<p class="salary"><b>Salary:</b> $ {{emp.salary}}</p>
	</div>
	{% endfor %}
</div>
```

4. You can add the optional styling which is included in my **index.html** page.

<br/>

## Check the **employees** page. For checking go to the following link:

```
http://localhost:8000/employees/
```

## In the end our site will something like this:

![](https://i.postimg.cc/prRzPhnn/Screenshot-from-2020-08-24-19-39-02.png)
