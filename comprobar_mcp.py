"""Consulta directa de la herramienta MCP de requisitos."""

import asyncio

from mcp import Client
from mcp.types import TextContent

from mcp_requisitos import mcp


async def ejecutar() -> None:
    async with Client(mcp, mode="legacy") as sesion:
        respuesta = await sesion.call_tool("requisito_prioridad", {})
        if respuesta.is_error:
            raise RuntimeError("No fue posible consultar el catálogo MCP")
        contenido = "\n".join(x.text for x in respuesta.content if isinstance(x, TextContent))
        print("Servidor: CatalogoRequisitosCarlos")
        print("Tool: requisito_prioridad")
        print("Lectura autorizada:", contenido)


if __name__ == "__main__":
    asyncio.run(ejecutar())
