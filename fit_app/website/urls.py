from django.contrib import admin
from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('samples/', views.samples, name='samples'),
    path('BMI_calculator/', views.BMI_calculator, name='BMI_calculator'),
]
