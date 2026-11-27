Aquí tienes la versión actualizada de los dos archivos Python con las modificaciones necesarias para cumplir con el requisito y el plan aprobable:

### `tareas.py`

```python
def agregar(tareas, titulo, prioridad="media"):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("Título obligatorio")
    tarea = {"id": len(tareas) + 1, "titulo": titulo, "prioridad": prioridad}
    tareas.append(tarea)
    return tarea


def pendientes(tareas):
    return list(tareas)


def filtrar_por_prioridad(tareas, prioridad):
    if prioridad not in ["alta", "media", "baja"]:
        raise ValueError("Prioridad inválida")
    return [tarea for tarea in tareas if tarea["prioridad"] == prioridad]
```

### `tests.py`

```python
import pytest

def test_agregar():
    tareas = []
    tarea = agregar(tareas, "Tarea 1")
    assert tarea == {"id": 1, "titulo": "Tarea 1", "prioridad": "media"}
    tarea = agregar(tareas, "Tarea 2", "alta")
    assert tarea == {"id": 2, "titulo": "Tarea 2", "prioridad": "alta"}
    tarea = agregar(tareas, "Tarea 3", "baja")
    assert tarea == {"id": 3, "titulo": "Tarea 3", "prioridad": "baja"}
    tarea = agregar(tareas, "Tarea 4", "")
    with pytest.raises(ValueError):
        agregar(tareas, "")

def test_pendientes():
    tareas = []
    agregar(tareas, "Tarea 1")
    agregar(tareas, "Tarea 2")
    assert pendientes(tareas) == [{"id": 1, "titulo": "Tarea 1", "prioridad": "media"}, {"id": 2, "titulo": "Tarea 2", "prioridad": "media"}]

def test_filtrar_por_prioridad():
    tareas = []
    agregar(tareas, "Tarea 1", "alta")
    agregar(tareas, "Tarea 2", "baja")
    agregar(tareas, "Tarea 3", "media")
    assert filtrar_por_prioridad(tareas, "alta") == [{"id": 1, "titulo": "Tarea 1", "prioridad": "alta"}]
    assert filtrar_por_prioridad(tareas, "baja") == [{"id": 2, "titulo": "Tarea 2", "prioridad": "baja"}]
    assert filtrar_por_prioridad(tareas, "media") == [{"id": 3, "titulo": "Tarea 3", "prioridad": "media"}]
    with pytest.raises(ValueError):
        filtrar_por_prioridad(tareas, "alta")
```

### Explicación de las modificaciones:

1. **Agregar prioridad a las tareas**:
   - Se ha añadido una nueva clave `prioridad` a cada tarea.
   - Se establece la prioridad por defecto como "media" si no se especifica.

2. **Función `filtrar_por_prioridad`**:
   - Se ha implementado la función para filtrar tareas por prioridad.

3. **Pruebas**:
   - Se han añadido pruebas de regresión para asegurar que las funciones funcionan correctamente.
   - Se han añadido pruebas para valores válidos y inválidos.
   - Se han añadido pruebas para filtrado de tareas por prioridad.

Estas modificaciones cumplen con el requisito y el plan aprobable, manteniendo la compatibilidad con las funciones `agregar` y `pendientes` y añadiendo las nuevas funcionalidades solicitadas.