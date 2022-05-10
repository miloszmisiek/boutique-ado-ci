""" We created this file as a shell for urls in home,
    it was copy-pasted from main urls.py, include was deleted and views imported """
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # empty path ('') indicates that it is root URL
    path('', views.index, name='home')
]
