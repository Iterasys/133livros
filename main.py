
def dizer_oi(nome):
    print(f'Olá, {nome}')


def somar_2_numeros(numero1, numero2):
    return numero1 + numero2


def multiplicar_2_numeros(numero1, numero2):
    return numero1 * numero2

def dividir_2_numeros(numero1, numero2):
    try:                # tente fazer
        return numero1 / numero2
    except ZeroDivisionError:
        return 'divisao por zero'





if __name__ == '__main__':  # acionador da execução do script
    dizer_oi('José Correia')

    '''
    numero1 = 17
    numero2 = 90
    resultado = somar_2_numeros(numero1, numero2)
    print(f'A soma de {numero1} e {numero2} é igual a {resultado}')
    print(f'{numero1}+{numero2}={resultado}')
    '''

    # Soma

    resultado = somar_2_numeros(20, 30)
    print(f'O resultado da soma é {resultado}')

    # Multiplicação
    resultado = multiplicar_2_numeros(3, 5)
    print(f'O resultado da multiplicação é {resultado}')

    # Divisão
    resultado = dividir_2_numeros(8, 4)
    print(f'O resultado da divisão é {resultado}')
