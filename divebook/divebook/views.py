"""Project-level views for the divebook site."""

from django.shortcuts import render


def homepage(request):
    """Render the home page template."""
    return render(request, "home.html")


def contact(request):
    """Render the contact page with a simple HTML form."""
    return render(request, "contact.html")
