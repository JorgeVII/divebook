"""Views for the trips app."""

from django.shortcuts import render


def divetrips_list(request):
    """Render the page that lists the available dive trips."""
    request.session["visitas"] = (
        request.session.get("visitas", 0) + 1
    )  # New line for UT5 user visit
    return render(request, "divetrips/divetrips_list.html")
