"""Project-level views for the divebook site."""

from django.shortcuts import render


def homepage(request):
    """Render the home page template."""
    return render(request, "home.html")
