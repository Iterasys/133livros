import unittest

import calculos


class MyTestCase(unittest.TestCase):
    def testar_subtrair_2_numeros(self):
        # Prepara / Configura
        numeroA = 3500
        numeroB = 1500
        resultado_esperado = 2000

        # Executa
        resultado_obtido = calculos.subtrair_2_numeros(numeroA,numeroB)

        # Valida / Compara
        self.assertEqual(resultado_esperado, resultado_obtido)  # add assertion here


if __name__ == '__main__':
    unittest.main()
