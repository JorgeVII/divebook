"""URL configuration for the trips app."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.divetrips_list, name="divetrips_list"),
]
