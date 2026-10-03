# CONTEXT.md - Registro de Interacción y Prompts con Herramientas de IA

Este documento registra los prompts y el contexto de interacción con herramientas de IA (Antigravity / Gemini) para el desarrollo, pruebas, métricas y aseguramiento de calidad del **Trabajo Práctico 11: Gestión de Calidad** (UADER FCyT - Ingeniería de Software 2).

---

## 1. Fase de Inspección y Métricas de Calidad
* **Objetivo:** Validar la detección de defectos de la Sesión 1 (inspección estática), el registro de sesiones, el cálculo de Phase Containment Effectiveness (PCE), densidad de defectos y parámetro TEP en Kanban.
* **Prompt principal utilizado:**
  > *"Inspección Estática (Sesión 1) y Registro de Sesiones está bien?"*
  > *"Las Métricas de Calidad y Cálculo de PCE (Phase Containment Effectiveness) están bien?"*
  > *"Está bien Parámetro TEP en Kanban (Tutorial Ing. A. Ruiz de Mendarozqueta)"*
  > *"Y esto estaría bien para el paso 1, 2 y 3?" [Imágenes de tablas R, F, T y RTMX adjuntas]*
* **Resultado obtenido:**
  - Detección precisa de 7 defectos en inspección de código y 2 en inspección de casos de test.
  - Formulación de PCE por fase (Inspección 75%, Unitario 16.7%, Funcional 8.3%) y formal canónica.
  - Corrección conceptual crítica del acrónimo TEP en el tutorial de Mendarozqueta: *Trabajo En Progreso* (WIP) y Ley de Little.
  Corrección de la respuesta de N=1999 (retorna 50 iteraciones).

---

## 3. Fase de Implementación de la Herramienta `json2csv.py` y DevOps
* **Objetivo:** Construir la herramienta de filtro Unix `json2csv.py`, estructurar el proyecto según CookieCutter, configurar linters, formateadores, tests con Pytest y workflow de CI/CD.
* **Prompt principal utilizado:**
  > *"Ayudame a planificar el código de json2csv.py, lo más simple y básico posible, cumpliendo con lo mínimo pedido"*
* **Resultado obtenido:**
  - Código modular y robusto de `json2csv.py` con soporte para stdin/stdout, archivos (`-i`, `-o`), delimitador configurable (`-d`) y manejo de UTF-8 con BOM.
