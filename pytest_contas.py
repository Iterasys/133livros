import pytest
import csv
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

def ler_dados_csv():
    dados_csv = []  # criamos uma lista vazia
    nome_arquivo = 'C:\\Users\\corre\\PycharmProjects\\133livros\\vendors\\massa_dividir_2_numeros.csv'
    try:
        with open(nome_arquivo, newline='') as arquivo_csv:
            campos = csv.reader(arquivo_csv, delimiter=';')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha não prevista: {fail}')


@pytest.mark.parametrize('id, numero1, numero2, resultado_esperado, tipo_teste', ler_dados_csv())
def teste_dividir_2_numeros(id, numero1, numero2, resultado_esperado, tipo_teste):
    # Configura
    # Valores vem da lista

    # Executa
    resultado_obtido = main.dividir_2_numeros(int(numero1), int(numero2))

    # Valida
    if tipo_teste == 'positivo':
        # Se o teste é do tipo positivo vai comparar os valores
        # Por isso converte o resultado_esperado para número (float)
        assert float(resultado_esperado) == resultado_obtido
    else:
        # Senão, o teste é negativo e vai comparar as mensagens de falha
        # Por isso não precisa converter
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



def teste_calcular_area_quadrado():
    # Configura
    lado = 3
    resultado_esperado = 9

    # Executa
    resultado_obtido = main.calcular_area_quadrado(lado)

    # Valida
    assert resultado_esperado == resultado_obtido


def teste_calcular_area_retangulo():
    # Configura
    largura = 5
    comprimento = 4
    resultado_esperado = 20

    # Executa
    resultado_obtido = main.calcular_area_retangulo(largura, comprimento)

    # Valida
    assert resultado_esperado == resultado_obtido


def teste_calcular_area_triangulo():
    # Configura
    largura = 10
    comprimento = 5
    resultado_esperado = 25

    # Executa
    resultado_obtido = main.calcular_area_triangulo(largura, comprimento)

    # Valida
    assert resultado_esperado == resultado_obtido







