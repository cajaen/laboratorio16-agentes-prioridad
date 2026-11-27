### Cambios mínimos y criterios verificables

1. **Agregar prioridad a las tareas**:
   - Agregar una nueva clave `prioridad` a cada tarea.
   - Establecer la prioridad por defecto como "media" si no se especifica.

2. **Función `filtrar_por_prioridad`**:
   - Implementar la función para filtrar tareas por prioridad.

3. **Pruebas**:
   - Pruebas de regresión para asegurar que las funciones funcionan correctamente.
   - Pruebas para valores válidos y inválidos.
   - Pruebas para filtrado de tareas por prioridad.

### Criterios verificables

1. **Agregar prioridad a las tareas**:
   - Tareas deben tener una clave `prioridad` con un valor de "alta", "media" o "baja".
   - Si no se especifica una prioridad, la prioridad debe ser "media".

2. **Función `filtrar_por_prioridad`**:
   - La función debe aceptar una lista de tareas y una prioridad.
   - Debe devolver una lista de tareas que coincidan con la prioridad especificada.

3. **Pruebas**:
   - Pruebas de regresión para asegurar que las funciones funcionan correctamente.
   - Pruebas para valores válidos y inválidos.
   - Pruebas para filtrado de tareas por prioridad.

### Pruebas

1. **Pruebas de regresión**:
   - Prueba que las funciones `agregar` y `pendientes` funcionan correctamente sin cambios.

2. **Pruebas para valores válidos**:
   - Prueba que se agregan tareas con diferentes prioridades.
   - Prueba que se agregan tareas sin prioridad y se asigna la prioridad por defecto.

3. **Pruebas para valores inválidos**:
   - Prueba que se lanza un `ValueError` si se intenta agregar una tarea sin título.

4. **Pruebas para filtrado de tareas por prioridad**:
   - Prueba que se filtran correctamente tareas por prioridad.
   - Prueba que se devuelven todas las tareas si se filtran por una prioridad desconocida.

### Implementación actualizada

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

### Pruebas adicionales

```python
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