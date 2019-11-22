# name of the file is strict with language.
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index)
]