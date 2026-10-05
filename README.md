# TP11: Gestión de Calidad - UADER FCyT

Proyecto correspondiente al **Trabajo Práctico 11: Gestión de Calidad** de la cátedra **Ingeniería de Software 2**, Licenciatura en Sistemas de Información, Facultad de Ciencia y Tecnología (UADER).

---

## Contenido del Proyecto

1. **Conjetura de Collatz (`collatz.py` / `src/tp11_is2/collatz.py`):**
   - Implementación verificada del algoritmo 3n + 1 para números en el rango 1 a 1999.
   - Manejo robusto de excepciones para entradas inválidas, tipos no enteros y límites de frontera.
2. **Filtro de Conversión JSON a CSV (`json2csv.py` / `src/tp11_is2/json2csv.py`):**
   - Herramienta de línea de comandos basada en la filosofía de filtros de Unix.
   - Soporte para flujos estándar `stdin` / `stdout` y archivos mediante `-i` y `-o`.
   - Delimitador configurable mediante `-d` (por defecto coma `,`).
   - Manejo seguro de excepciones y compatibilidad con UTF-8 y UTF-8 BOM.

---

## Estructura del Repositorio (CookieCutter Pattern)

              # Workflow de Integración Continua (CI/CD)
                    # Documentación técnica (pdoc / Sphinx)

       # Pruebas unitarias para Collatz (Pytest)
        # Pruebas unitarias para json2csv (Pytest)
                 # Exclusión de entornos virtuales y cachés
                     # Identificador del build actual
                # Historial de versiones y cambios
                 # Registro de prompts de IA
                   # Licencia MIT
                  # Descripción general y guía de uso
            # Dependencias del proyecto
            # Dependencias del proyecto
                   # Número de versión semántica (1.0.0)

---


## Guía de Uso

### Herramienta `json2csv.py`
* **Mediante tuberías (Filtro Unix):**
  ```bash
  cat datos.json | python json2csv.py
  ```
* **Con archivos de entrada y salida:**
  ```bash
  python json2csv.py -i datos.json -o salida.csv
  ```
* **Con delimitador personalizado:**
  ```bash
  python json2csv.py -i datos.json -o salida.csv -d ";"
  ```

### Script `collatz.py`
```bash
python collatz.py
```
Solicitará un número entero entre 1 y 1999 por teclado y reportará el número de partida y la cantidad de iteraciones hasta llegar a 1.

---

## Pruebas y Aseguramiento de Calidad

* **Ejecutar tests con reporte de cobertura:**
  ```bash
  pytest --cov=src --cov=. tests/
  ```
* **Linters y formato:**
  ```bash
  ruff check .
  black --check .
  mypy json2csv.py collatz.py
  bandit -r . -x ./venv
  ```

---

## Licencia

Este proyecto está bajo la Licencia **MIT** - consulte el archivo [LICENSE](LICENSE) para más detalles.
