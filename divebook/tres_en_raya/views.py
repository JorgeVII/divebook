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

    for a, b, c in WINNING_LINES:
        if tablero[a] != "-" and tablero[a] == tablero[b] == tablero[c]:
            return tablero[a]
    return None


def jugada_valida(tablero, turno, posicion):

    if len(tablero) != 9 or any(c not in "XO-" for c in tablero):
        return False
    if turno not in ("X", "O"):
        return False
    if posicion not in [str(n) for n in range(9)]:
        return False
    return tablero[int(posicion)] == "-"


def tres_en_raya(request):
    """Play tic-tac-toe keeping the board and the turn in the session."""

    if request.method == "GET":
        # UT5 T2 (visits): count the visit only when entering the page, not on every move
        request.session["visitas"] = request.session.get("visitas", 0) + 1
        # UT5 T2 (session): a GET starts a new game stored in the session
        request.session["tablero"] = EMPTY_BOARD
        request.session["turno"] = "X"

    # UT5 T2 (session): read the game from the session, not from the form
    tablero = request.session.get("tablero", EMPTY_BOARD)
    turno = request.session.get("turno", "X")
    mensaje = f"Turno de {turno}"
    terminado = False

    if request.method == "POST":
        # UT5 T2 (form): the only data coming from the form is the clicked cell
        posicion = request.POST.get("posicion", "")

        if calcular_ganador(tablero) or "-" not in tablero:
            # UT5 T2 (security): the game is over, no more moves are accepted
            mensaje = "La partida ha terminado"
            terminado = True
        elif jugada_valida(tablero, turno, posicion):
            casillas = list(tablero)
            casillas[int(posicion)] = turno
            tablero = "".join(casillas)

            ganador = calcular_ganador(tablero)
            if ganador:
                mensaje = f"¡Ha ganado {ganador}!"
                terminado = True
            elif "-" not in tablero:
                mensaje = "Empate"
                terminado = True
            else:
                turno = "O" if turno == "X" else "X"
                mensaje = f"Turno de {turno}"

            # UT5 T2 (session): save the updated board and turn in the session
            request.session["tablero"] = tablero
            request.session["turno"] = turno
        else:
            # UT5 T2 (session): the board is safe in the session, so it is kept instead of reset
            mensaje = f"Jugada no válida. Turno de {turno}"

    # UT5 T2 (context): the session data is sent to the template through the context
    contexto = {
        "tablero": tablero,
        "turno": turno,
        "mensaje": mensaje,
        "terminado": terminado,
    }
    return render(request, "tres_en_raya/tres_en_raya.html", contexto)
