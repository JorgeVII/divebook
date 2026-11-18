"""URL configuration for the tres_en_raya app."""

from django.urls import path

from . import views

app_name = "tres_en_raya"  # namespace

urlpatterns = [
    path("", views.tres_en_raya, name="play"),  # etiqueta root
]
