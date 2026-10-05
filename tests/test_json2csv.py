"""Pruebas unitarias para el modulo json2csv.py."""

import json

import pytest

from tp11_is2.json2csv import json_to_csv, main


def test_conversion_lista_objetos():
    """Convierte correctamente una lista de diccionarios a CSV."""
    entrada = json.dumps([{"id": 1, "nombre": "Lucas"}, {"id": 2, "nombre": "Ana"}])
    csv_res = json_to_csv(entrada)
    lineas = csv_res.strip().split("\n")
    assert lineas[0] == "id,nombre"
    assert lineas[1] == "1,Lucas"
    assert lineas[2] == "2,Ana"


def test_conversion_objeto_unico():
    """Convierte un único diccionario a CSV."""
    entrada = json.dumps({"producto": "Mouse", "precio": 25})
    csv_res = json_to_csv(entrada)
    lineas = csv_res.strip().split("\n")
    assert lineas[0] == "producto,precio"
    assert lineas[1] == "Mouse,25"


def test_delimitador_personalizado():
    """Usa el delimitador especificado (ej. punto y coma)."""
    entrada = json.dumps([{"a": 10, "b": 20}])
    csv_res = json_to_csv(entrada, delimiter=";")
    assert "a;b" in csv_res
    assert "10;20" in csv_res


def test_soporte_utf8_bom():
    """Soporta cadenas con BOM (comun en Windows / PowerShell)."""
    entrada = "\ufeff" + json.dumps([{"item": "PC"}])
    csv_res = json_to_csv(entrada)
    assert "item" in csv_res


def test_json_invalido():
    """Lanza ValueError ante JSON con sintaxis erronea."""
    with pytest.raises(ValueError, match="Formato JSON invalido"):
        json_to_csv("{invalido}")


def test_entrada_vacia():
    """Lanza ValueError ante entrada vacia."""
    with pytest.raises(ValueError, match="vacia"):
        json_to_csv("   ")


def test_estructura_no_objeto():
    """Lanza ValueError si el JSON no es un objeto o lista de objetos."""
    with pytest.raises(ValueError, match="debe contener un objeto"):
        json_to_csv("[1, 2, 3]")


def test_cli_stdin_stdout(monkeypatch, capsys):
    """Ejecucion de CLI mediante stdin y stdout."""
    monkeypatch.setattr("sys.argv", ["json2csv.py"])
    monkeypatch.setattr("sys.stdin.read", lambda: '[{"x": 1, "y": 2}]')
    main()
    captured = capsys.readouterr()
    assert "x,y" in captured.out
    assert "1,2" in captured.out


def test_cli_archivos_in_out(tmp_path, monkeypatch):
    """Ejecucion de CLI con argumentos -i y -o."""
    archivo_in = tmp_path / "in.json"
    archivo_out = tmp_path / "out.csv"
    archivo_in.write_text('[{"col1": "val1"}]', encoding="utf-8")

    monkeypatch.setattr(
        "sys.argv", ["json2csv.py", "-i", str(archivo_in), "-o", str(archivo_out)]
    )
    main()

    contenido = archivo_out.read_text(encoding="utf-8")
    assert "col1" in contenido
    assert "val1" in contenido


def test_cli_archivo_inexistente(monkeypatch):
    """Manejo de error y codigo de salida ante archivo no encontrado."""
    monkeypatch.setattr(
        "sys.argv", ["json2csv.py", "-i", "archivo_que_no_existe_123.json"]
    )
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1
