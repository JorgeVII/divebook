"""Views for the tres_en_raya app."""

from django.shortcuts import render


def tres_en_raya(request):
    """Show the tic-tac-toe board with its initial state."""
    tablero = "---------"
    turno = "X"
    mensaje = "Turno de X"
    terminado = False

    contexto = {
        "tablero": tablero,
        "turno": turno,
        "mensaje": mensaje,
        "terminado": terminado,
    }
    return render(request, "tres_en_raya/tres_en_raya.html", contexto)
