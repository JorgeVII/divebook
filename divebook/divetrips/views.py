"""Views for the trips app."""

from django.shortcuts import render


def divetrips_list(request):
    """Render the page that lists the available dive trips."""
    return render(request, "divetrips/divetrips_list.html")
