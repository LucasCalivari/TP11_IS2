# CHANGELOG.md - Historial de Cambios

Todas las modificaciones notables realizadas en este proyecto serán documentadas en este archivo.
El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/) y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

---

## [1.0.0] - 2026-10-03 (Build: 2026.10.03.01)

### Agregado
- Implementación del script `collatz.py` con validación de rango 1 a 1999, cálculo de iteraciones y manejo de excepciones.
- Implementación de la herramienta de filtro Unix `json2csv.py` para conversión de JSON a CSV:
  - Soporte de argumentos por línea de comandos `-i`, `-o`, `-d`.
  - Fallback a flujos estándar `sys.stdin` y `sys.stdout`.
  - Soporte para codificación UTF-8 estándar y UTF-8 con BOM (`utf-8-sig`).
  - Tratamiento robusto de excepciones ante archivos inexistentes y JSON inválido.
- Suite de pruebas unitarias y funcionales con `pytest` y cobertura de código.
- Estructura CookieCutter con directorios `src/`, `tests/`, `docs/`, `.github/workflows/`.
- Archivos de metadatos y trazabilidad: `VERSION`, `BUILD`, `CONTEXT.md`, `REQUIREMENTS.TXT`.
- Configuración de flujo de Integración Continua (CI/CD) con GitHub Actions.

### Corregido
- Corrección de defectos sintácticos en `collatz.py` (resolución de `return iter`, llamada a variable indefinida `j`, desbalance de paréntesis en llamada `print`).
- Corrección del resultado esperado de la conjetura de Collatz para N=1999 (establecido en 50 iteraciones).
