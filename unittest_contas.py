# 1 - Bibliotecas
import unittest  # Essa biblioteca será baixada automaticamente pelo PIP
import main      # referencia ao arquivo main.py

# 2 - Classes (Grupo de definitions)
class Casos_de_teste(unittest.TestCase):
    # 3 - Métodos e Funções


    def teste_multiplicar_2_numeros(self):
        # A - Configura
        numero1 = 2
        numero2 = 3
        resultado_esperado = 6

        # B - Executa
        resultado_obtido = main.multiplicar_2_numeros(numero1, numero2)

        # C - Valida
        self.assertEqual(resultado_esperado, resultado_obtido)  # add assertion here

    def teste_somar_2_numeros(self):
        numero1 = 7
        numero2 = 8
        resultado_esperado = 16

        resultado_obtido = main.somar_2_numeros(numero1, numero2)

        self.assertEqual(resultado_esperado, resultado_obtido)

if __name__ == '__main__':
    unittest.main()
