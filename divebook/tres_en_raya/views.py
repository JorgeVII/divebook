"""Views for the tres_en_raya app."""

from django.shortcuts import render

EMPTY_BOARD = "---------"


WINNING_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),  # finas
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),  # columns
    (0, 4, 8),
    (2, 4, 6),  # diagonales
]


def calcular_ganador(tablero):
    """Return 'X' or 'O' if a player has three in a row, otherwise None."""
    for a, b, c in WINNING_LINES:
        if tablero[a] != "-" and tablero[a] == tablero[b] == tablero[c]:
            return tablero[a]
    return None


def jugada_valida(tablero, turno, posicion):
    """Check that the data received from the form is a legal move."""
    if len(tablero) != 9 or any(c not in "XO-" for c in tablero):
        return False
    if turno not in ("X", "O"):
        return False
    if posicion not in [str(n) for n in range(9)]:
        return False
    return tablero[int(posicion)] == "-"


def tres_en_raya(request):
    """Show the board and, when the form is sent, apply the chosen move."""

    tablero = EMPTY_BOARD
    turno = "X"
    mensaje = "Turno de X"
    terminado = False

    if request.method == "POST":
        tablero_recibido = request.POST.get("tablero", "")
        turno_recibido = request.POST.get("turno", "")
        posicion = request.POST.get("posicion", "")

        if jugada_valida(tablero_recibido, turno_recibido, posicion):
            casillas = list(tablero_recibido)
            casillas[int(posicion)] = turno_recibido
            tablero = "".join(casillas)

            ganador = calcular_ganador(tablero)
            if ganador:
                mensaje = f"¡Ha ganado {ganador}!"
                terminado = True
            elif "-" not in tablero:
                mensaje = "Empate"
                terminado = True
            else:
                turno = "O" if turno_recibido == "X" else "X"
                mensaje = f"Turno de {turno}"
        else:
            mensaje = "Jugada no válida: se ha reiniciado la partida. Turno de X"

    contexto = {
        "tablero": tablero,
        "turno": turno,
        "mensaje": mensaje,
        "terminado": terminado,
    }
    return render(request, "tres_en_raya/tres_en_raya.html", contexto)
