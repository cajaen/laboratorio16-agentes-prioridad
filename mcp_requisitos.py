"""Catálogo MCP de requisitos aprobados para la práctica."""

from mcp.server import MCPServer


mcp = MCPServer("CatalogoRequisitosCarlos")


@mcp.tool()
def requisito_prioridad() -> str:
    """Entrega la regla autorizada sin modificar archivos ni ejecutar acciones."""
    return (
        "La tarea admite prioridad alta, media o baja y usa media cuando no se indica. "
        "Una prioridad desconocida produce ValueError. "
        "Debe existir filtrar_por_prioridad(tareas, prioridad). "
        "Las funciones agregar y pendientes mantienen compatibilidad. "
        "Las pruebas cubren regresión, valores válidos, inválidos y filtrado."
    )
