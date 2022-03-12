import pytest

import main

lista_para_multiplicar = [
    (2, 3, 6),
    (0, 4, 0),
    (-5, -3, 15),
    (8, 1000, 8000),
    (7, '', ''),
    (9, ' ', '         '),
    (10, 'a', 'aaaaaaaaaa')
]
@pytest.mark.parametrize('numero1, numero2, resultado_esperado', lista_para_multiplicar)
def teste_multiplicar_2_numeros(numero1, numero2, resultado_esperado):
    # Configura - virá da lista

    # Executa
    resultado_obtido = main.multiplicar_2_numeros(numero1, numero2)

    # Valida
    assert resultado_obtido == resultado_esperado



lista_para_dividir = [
    (8, 4, 2),
    (9, 3, 3),
    (9, 2, 4.5),
    (8, 0, 'divisao por zero')
]
@pytest.mark.parametrize('numero1, numero2, resultado_esperado', lista_para_dividir)
def teste_dividir_2_numeros(numero1, numero2, resultado_esperado):
    # Configura
    # Valores vem da lista

    # Executa
    resultado_obtido = main.dividir_2_numeros(numero1, numero2)

    # Valida
    assert resultado_esperado == resultado_obtido

lista_para_calcular_areas = [
    (10, 15, 150),
    (7, 0, 'um ou ambos os valores de largura e comprimento são zero ou negativos'),
    (5, -7, 'um ou ambos os valores de largura e comprimento são zero ou negativos'),
    (6, 'a', 'um ou ambos os valores de largura e comprimento são letras')
]
@pytest.mark.parametrize('largura, comprimento, resultado_esperado', lista_para_calcular_areas)
def teste_calcular_area(largura, comprimento, resultado_esperado):
    # Configura vem da lista

    # Executa
    resultado_obtido = main.calcular_area(largura, comprimento)

    # Valida
    assert resultado_obtido == resultado_esperado












