"""URL configuration for the usuarios app."""

from django.urls import path

from . import views

app_name = "usuarios"  # UT5 T3 (users): namespace

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("registro/", views.registro, name="registro"),
    path("login/", views.iniciar_sesion, name="iniciar_sesion"),
]
