NIVELES_VALIDOS = frozenset({"alta", "media", "baja"})


def _limpiar_titulo(titulo):
    limpio = titulo.strip()
    if not limpio:
        raise ValueError("Título obligatorio")
    return limpio


def _comprobar_nivel(prioridad):
    if prioridad not in NIVELES_VALIDOS:
        raise ValueError(f"Prioridad desconocida: {prioridad}")


def agregar(tareas, titulo, prioridad="media"):
    titulo_limpio = _limpiar_titulo(titulo)
    _comprobar_nivel(prioridad)
    tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo_limpio,
        "prioridad": prioridad,
    }
    tareas.append(tarea)
    return tarea


def pendientes(tareas):
    return list(tareas)


def filtrar_por_prioridad(tareas, prioridad):
    _comprobar_nivel(prioridad)
    return [registro.copy() for registro in tareas if registro.get("prioridad") == prioridad]
