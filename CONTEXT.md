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

---

## 4. Fase de Verificación, Modelos de Confiabilidad y Testing Unitario (Puntos 8, 9, 12 y 13)
* **Objetivo:** R verificar los Puntos 8, 9, 12 y 13 del TP11, formalizar hipótesis de test unitario y ejecutar la suite completa en Pytest asegurando cobertura >= 855.
* **Prompt principal utilizado:**
  > *"verica los puntos 8, 9, 12 y 13. Ejecuta pruebas unitarias con Pytest (Cobertura >= 85%) (Test unitario con Pytest con hipótesis de test unitario que permitan la cobertura del 85% o mejor.)."*
* **Resultado obtenido:**
  - Verificación formal de las 3 condiciones de parada del Punto 8 con matriz RTMX íntegra.
  - Consolidación del listado de 6 sesiones y 12 defectos detectados (Punto 9).
  - Ejecución de 23 pruebas unitarias y funcionales en Pytest alcanzando una cobertura del 100% (superando ampliamente el umbral del 85%).

