"""Views for the usuarios app: sign up and log in."""

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def inicio(request):
    """Show the users page with links to log in and sign up."""
    # UT5 T3 (users): hub page so the nav only needs one link
    return render(request, "usuarios/inicio.html")


def registro(request):
    """Show the sign up form and create the user if the data is valid."""
    if request.method == "POST":
        # UT5 T3 (sign up): form filled with the data the user sent
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # UT5 T3 (sign up): creates the user in the database
            return redirect("usuarios:iniciar_sesion")
    else:
        # UT5 T3 (sign up): empty form when the user just enters the page
        form = UserCreationForm()

    # UT5 T3 (sign up): reached on GET or when the form has errors
    return render(request, "usuarios/registro.html", {"form": form})


def iniciar_sesion(request):
    """Show the log in form and start the session if the credentials are right."""
    if request.method == "POST":
        # UT5 T3 (log in): request first, then the data the user sent
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())  # UT5 T3 (log in): starts the session
            return redirect("homepage")
    else:
        form = AuthenticationForm(request)

    # UT5 T3 (log in): reached on GET or when user/password are wrong
    return render(request, "usuarios/iniciar_sesion.html", {"form": form})
