"""Project-level views for the divebook site."""

from django.http import HttpResponse


def homepage(request):
    """Return a plain text response for the home page."""
    return HttpResponse("Hello World!")
