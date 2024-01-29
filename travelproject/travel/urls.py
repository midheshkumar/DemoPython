from . import views
from django.urls import path

app_name='travel'

urlpatterns = [
    path('',views.demo,name='demo'),
    #path('add/',views.addition,name='addition'),


]
