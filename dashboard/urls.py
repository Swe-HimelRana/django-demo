from django.contrib import admin
from django.urls import path
from .views import index, chart, countries
urlpatterns = [
    path('', index, name='dashboard'),
    path('chart/', chart, name='chart'),
    path('countries/', countries, name='countries'),

]
