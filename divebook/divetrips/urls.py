"""URL configuration for the trips app."""

from django.urls import path

from . import views

app_name = "divetrips"

urlpatterns = [
    path("", views.divetrips_list, name="list"),
]
