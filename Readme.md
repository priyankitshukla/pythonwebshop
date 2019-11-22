# Install Django using terminal

# pip install django==2.1
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
