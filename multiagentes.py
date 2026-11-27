"""Coordinación de tres roles con traspasos mediante archivos de evidencia."""

from __future__ import annotations

import asyncio
import subprocess
import sys
from pathlib import Path

from mcp import Client
from mcp.types import TextContent
from ollama import chat

from mcp_requisitos import mcp


MODELO_LOCAL = "qwen2.5-coder:3b"
CARPETA_EVIDENCIAS = Path("evidencias")
CARPETA_EVIDENCIAS.mkdir(exist_ok=True)


async def obtener_especificacion() -> str:
    async with Client(mcp, mode="legacy") as sesion:
        resultado = await sesion.call_tool("requisito_prioridad", {})
        if resultado.is_error:
            raise RuntimeError("La consulta MCP fue rechazada")
        partes = [parte.text for parte in resultado.content if isinstance(parte, TextContent)]
        if not partes:
            raise RuntimeError("La herramienta no entregó contenido textual")
        return "\n".join(partes)


def pedir_revision(instrucciones: str, contexto: str) -> str:
    mensaje = chat(
        model=MODELO_LOCAL,
        messages=[
            {"role": "system", "content": instrucciones},
            {"role": "user", "content": contexto},
        ],
        options={"temperature": 0, "seed": 61},
    )
    return mensaje.message.content or ""


async def preparar_cambio() -> None:
    especificacion = await obtener_especificacion()
    fuente = Path("tareas.py").read_text(encoding="utf-8")
    estrategia = pedir_revision(
        "Actúa como arquitecto planificador. Enumera cambios mínimos, criterios verificables y pruebas. "
        "No entregues código ni amplíes el alcance autorizado.",
        f"ESPECIFICACIÓN MCP:\n{especificacion}\n\nIMPLEMENTACIÓN INICIAL:\n{fuente}",
    )
    (CARPETA_EVIDENCIAS / "01_plan.md").write_text(estrategia, encoding="utf-8")
    borrador = pedir_revision(
        "Actúa como programador implementador. Devuelve versiones completas de los dos archivos Python. "
        "Mantén compatibilidad, evita dependencias y no propongas acciones de terminal.",
        f"REQUISITO:\n{especificacion}\n\nPLAN APROBABLE:\n{estrategia}\n\nBASE:\n{fuente}",
    )
    (CARPETA_EVIDENCIAS / "02_propuesta.md").write_text(borrador, encoding="utf-8")
    print("Plan guardado en evidencias/01_plan.md")
    print("Borrador guardado en evidencias/02_propuesta.md")
    print("Ningún archivo del proyecto fue modificado por los agentes.")


async def auditar_cambio() -> None:
    especificacion = await obtener_especificacion()
    resultado = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    paquete = (
        f"REQUISITO:\n{especificacion}\n\n"
        f"TAREAS.PY:\n{Path('tareas.py').read_text(encoding='utf-8')}\n\n"
        f"PRUEBAS:\n{Path('tests/test_tareas.py').read_text(encoding='utf-8')}\n\n"
        f"EJECUCIÓN (código {resultado.returncode}):\n{resultado.stdout}{resultado.stderr}"
    )
    dictamen = pedir_revision(
        "Actúa como revisor técnico. Comprueba requisito, regresión, pruebas, seguridad y alcance. "
        "Diferencia evidencia de opinión y señala cualquier pendiente.",
        paquete,
    )
    (CARPETA_EVIDENCIAS / "03_revision.md").write_text(dictamen, encoding="utf-8")
    print("Código de salida de pruebas:", resultado.returncode)
    print("Dictamen guardado en evidencias/03_revision.md")


if __name__ == "__main__":
    seleccion = sys.argv[1].lower() if len(sys.argv) > 1 else input("Modo (proponer/revisar): ").strip().lower()
    if seleccion not in {"proponer", "revisar"}:
        raise SystemExit("Modo válido: proponer o revisar")
    asyncio.run(auditar_cambio() if seleccion == "revisar" else preparar_cambio())
