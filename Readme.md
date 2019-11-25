# Install Django using terminal

# pip install django==2.1.5
#  django-admin startproject pythonwebshop .
# check the installation by running the server command - python manage.py runserver


########### to create  specific app/module this should create another module in the project

#  python manage.py startapp products


# creating a end point example is based on products module


# Step 1 - def a function in views.py of the module need to import HTTPResponse from django.http
# Step 2-  create  a file in the folder with name urls.py to map the endpoints.
# Step 3 - add an entry for path in urls.py import path from django.urls
# Step 4-  connect it with base project make an additional entry in urls.py
# Step 5- to access current exercise http://localhost:8000/products
# Step 6 - home page will disappear after this.



# Download sqllite browser https://sqlitebrowser.org/dl/
# migration >python manage.py makemigrations
# above command will create a file in migration folder for creating models and other stuff
# To generate the tables in database use command >python manage.py migrate



# Admin
# use url localhost:8000/admin to access the admin page.
# create a super user python manage.py createsuperuser

# for now create using admin/admin

# once we are logged in we will get list of group and users but we can simply manage products as well.py


############## check sqllite version

#>>> import sqlite3
#>>> sqlite3.version
#'2.3.2'
#>>> sqlite3.sqlite_version
#'3.3.4'
#
#
#

<!-- {% %} is statndard django tempate -->
<!-- use double curly braces to render content dynamically -->

# To show products in public domain ie- out of admin module

Step 1- go to views and import the products

Step 2- inside the def call Product.object.all() to get all records we can use filter and other inbuilt methods to it.products

Step 3- Create a folder named as templates make sure name is same

Step 4- Create a basic file index.html inside the templates

Step 5- now send the object from the view from the render method like

 products=Product.objects.all()
     return render(request, 'index.html'
                   ,{'products':products})


Install bootstrap

Step 1- create a file name base.html

Step 2- go to https://getbootstrap.com/docs/4.3/getting-started/introduction/ and copy the code for base tempate

Step 3- Inside body section create a django template tag with block and name it as content
            like
             {%  block content %}
                {%  endblock %}

Step 4- import base file in index.html

 like -
 ```python
 {% extends 'base.html' %}
{% block content%}
    <h1>Products</h1>
    <ul>
        {% for product in products %}
             <li>{{product.name}} ({{ product.price}})</li>
        {% endfor %}

    </ul>

{% endblock %}

```python
