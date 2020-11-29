from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("", views.company, name = "company"),
    path("A/", views.A, name="A"),
    path("insert/", views.insert, name="insert"),
]
