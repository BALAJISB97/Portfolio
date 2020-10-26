from django.contrib import admin
from django.urls import include, path
from homeapp import views

urlpatterns = [
    path('', views.home,name='home'),
    path('contact',views.contact,name='contact')
]
