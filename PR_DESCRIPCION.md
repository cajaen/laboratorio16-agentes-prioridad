# Incorporación de prioridades y filtro

## Propósito

Extender el registro de tareas con prioridades controladas y conservar el comportamiento anterior.

## Especificación consultada

`requisito_prioridad` se obtuvo desde un servidor MCP de solo lectura y se utilizó como límite del cambio.

## Evidencias enlazadas

- Plan del agente: `evidencias/01_plan.md`
- Propuesta del implementador: `evidencias/02_propuesta.md`
- Dictamen del revisor: `evidencias/03_revision.md`
- Comprobación MCP: `evidencias/04_prueba_mcp.txt`
- Pruebas finales: `evidencias/05_pruebas_finales.txt`

## Riesgos y controles

La propuesta generada puede contener errores. El código aplicado fue delimitado, revisado y probado por una persona antes del commit. El token de Actions solo necesita lectura.

## Lista de revisión

- [x] Tres prioridades permitidas
- [x] Valor medio por defecto
- [x] Rechazo con `ValueError`
- [x] Filtro y regresión cubiertos
- [x] Sin secretos, despliegues ni comandos dinámicos
