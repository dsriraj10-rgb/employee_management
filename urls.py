from django.contrib import admin
from django.urls import path, include
from .views import employee_home, addEmp
urlpatterns = [
    path('home/', employee_home),
    path('addEmp/', addEmp),
] 