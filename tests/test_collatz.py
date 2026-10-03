"""Pruebas unitarias para el modulo collatz.py."""

import pytest

from collatz import collatz, main


def test_t1_caso_base():
    """T1: Caso base N=1 debe retornar 0 iteraciones."""
    assert collatz(1) == 0


def test_t2_alternancia_par_impar():
    """T2: N=20 cubre ramas par e impar y retorna 7 iteraciones."""
    assert collatz(20) == 7


def test_t3_limite_superior_valido():
    """T3: N=1999 limite superior permitido debe retornar 50 iteraciones."""
    assert collatz(1999) == 50


def test_t4_cero_y_negativos():
    """T4: N=0 y valores negativos deben lanzar ValueError."""
    with pytest.raises(ValueError):
        collatz(0)
    with pytest.raises(ValueError):
        collatz(-5)


def test_t5_excede_limite_maximo():
    """T5: N=2000 excede el limite de 1999 y debe lanzar ValueError."""
    with pytest.raises(ValueError):
        collatz(2000)


def test_tipos_invalidos():
    """Validacion de tipos: no enteros o flotantes deben lanzar ValueError."""
    with pytest.raises(ValueError):
        collatz("texto")  # type: ignore
    with pytest.raises(ValueError):
        collatz(12.5)  # type: ignore
    with pytest.raises(ValueError):
        collatz(True)  # type: ignore


def test_main_exitoso(monkeypatch, capsys):
    """Prueba funcional de main con entrada valida."""
    monkeypatch.setattr("builtins.input", lambda _: "20")
    main()
    captured = capsys.readouterr()
    assert "El numero de partida es 20 y el numero de iteraciones es 7." in captured.out


def test_main_error_validacion(monkeypatch, capsys):
    """Prueba funcional de main con entrada invalida."""
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    main()
    captured = capsys.readouterr()
    assert "Error de validacion" in captured.out
