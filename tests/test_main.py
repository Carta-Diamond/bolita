import pytest

from main import calcular_area_triangulo

def test_area_triangulo():
    #Resultado obtenido(real)
    actual_result = calcular_area_triangulo(13, 3)

    #assert (estamos verificando) que el resultado obtenido sea aproximadamente igual a 19.5 con una tolerancia de 0.01
    assert actual_result == pytest.approx(19.5, abs=0.01)

