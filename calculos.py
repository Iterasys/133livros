def subtrair_2_numeros(numeroA, numeroB):
    resultado = numeroA - numeroB
    return resultado

if __name__ == '__main__':  # acionador / gatilho
    print('Calculos')
    resultado = subtrair_2_numeros(15,9)
    print(f'O resultado da subtração é: {resultado}')