from django.contrib import admin
from django.urls import path

from . import views

app_name = 'calculators'

urlpatterns = [
    path('BMI_calculator/', views.BMI_calculator, name='BMI_calculator'),
]
