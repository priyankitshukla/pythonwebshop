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

