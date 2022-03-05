
def dizer_oi(nome):
    print(f'Olá, {nome}')


def somar_2_numeros(numero1, numero2):
    return numero1 + numero2


if __name__ == '__main__':  # acionador da execução do script
    dizer_oi('José Correia')

    '''
    numero1 = 17
    numero2 = 90
    resultado = somar_2_numeros(numero1, numero2)
    print(f'A soma de {numero1} e {numero2} é igual a {resultado}')
    print(f'{numero1}+{numero2}={resultado}')
    '''

    resultado = somar_2_numeros(17, 90)
    print(f'O resultado é {resultado}')