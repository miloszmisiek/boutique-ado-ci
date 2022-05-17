""" We created this file as a shell for urls in bag,
    it was copy-pasted from home urls.py, include was deleted and views imported """
from django.urls import path
from . import views

urlpatterns = [
    # empty path ('') indicates that it is root URL
    path('', views.view_bag, name='view_bag')
]
