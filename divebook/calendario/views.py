"""Views for the calendario app."""

from datetime import date, datetime

from django.shortcuts import render

MESES = [
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre",
]
DIAS_SEMANA = [
    "lunes",
    "martes",
    "miércoles",
    "jueves",
    "viernes",
    "sábado",
    "domingo",
]


def calendario(request, fecha):
    """
    Show details about a date given in the URL as DD-MM-YYYY.

    If the text is not a valid date, render an error page instead.
    """
    request.session["visitas"] = request.session.get("visitas", 0) + 1
    try:
        fecha_objeto = datetime.strptime(fecha, "%d-%m-%Y").date()
    except ValueError:
        return render(
            request,
            "calendario/error.html",
            {"fecha": fecha},
            status=400,
        )

    mi_dia = fecha_objeto.day
    mi_mes = MESES[fecha_objeto.month - 1]
    mi_ano = fecha_objeto.year

    dia_semana = DIAS_SEMANA[fecha_objeto.weekday()]
    hoy = date.today()
    if fecha_objeto == hoy:
        referencia = "Es hoy"
    elif fecha_objeto < hoy:
        referencia = "Ya ha pasado"
    else:
        referencia = "Todavía no ha llegado"
    mensaje = f"Cae en {dia_semana}. {referencia}."

    return render(
        request,
        "calendario/fecha.html",
        {"dia": mi_dia, "mes": mi_mes, "ano": mi_ano, "mensaje": mensaje},
    )
