"""URL configuration for the calendario app."""

from django.urls import path

from . import views

app_name = "calendario"

urlpatterns = [
    path("<str:fecha>/", views.calendario, name="calendario"),
]
