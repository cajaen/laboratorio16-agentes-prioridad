# Registro de tareas priorizadas

Implementación del Laboratorio 16 con tres roles separados y traspasos mediante evidencias. El catálogo MCP solo expone el requisito autorizado; ningún agente escribe código del proyecto, ejecuta comandos variables ni publica cambios.

## Preparación

```cmd
python -m pip install -r requirements.txt
ollama pull qwen2.5-coder:3b
```

## Flujo de comprobación

```cmd
python comprobar_mcp.py
python multiagentes.py proponer
python -m unittest discover -s tests -v
python multiagentes.py revisar
```

GitHub Actions separa la verificación del PR y la creación del artefacto posterior al merge. Crear un paquete no equivale a desplegarlo.
