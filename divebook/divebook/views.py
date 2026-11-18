"""Project-level views for the divebook site."""

from django.shortcuts import render


def homepage(request):
    """Render the home page template."""
    request.session["visitas"] = (
        request.session.get("visitas", 0) + 1
    )  # New line for UT5 user visit
    return render(request, "home.html")


def contact(request):
    """Render the contact page with a simple HTML form."""
    request.session["visitas"] = (
        request.session.get("visitas", 0) + 1
    )  # New line for UT5 user visit
    return render(request, "contact.html")
