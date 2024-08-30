import os

'''
n = divideNdo | d = Divisor | q = Quociente | r = Resto | x = resultado

nn = nome pro valor do dividendo + separador ("x" é o argumento padrão para
o separador)

dd = nome pro valor do divisor
'''

def divisao_equilibrada(n, d, nn='x', dd=''):
    q = n // d
    r = n % d

    if r == 0:
        return f'{q} {nn} {d} {dd}'

    return f'{q} {nn} {(d - r)} {dd}\n{(q + 1)} {nn} {r} {dd}'


while True:
    try:
        entrada = input(
            '\nDigite "I" para iniciar a operação ou "P" para parar: '
        )

        if entrada.lower() == 'i':
            print('\nCalculadora v0.6.0\n')
            resultado = float(input('Primeiro número:\n'))

            while True:
                operador = input('\nOperador (ou "F" para finalizar):\n')

                if operador.lower() == 'f':
                    break

                if operador in ['+', '-', '*', '/', '//', '**', '%', '%%']:
                    num = float(input('\nPróximo número:\n'))
                    if operador == '+':
                        resultado += num
                    elif operador == '-':
                        resultado -= num
                    elif operador == '*':
                        resultado *= num
                    elif operador == '/':
                        resultado /= num
                    elif operador == '//':
                        resultado //= num
                    elif operador == '**':
                        resultado **= num
                    elif operador == '%':
                        resultado %= num
                    elif operador == '%%':
                        os.system('cls')
                        print(
                            f'\nResultado:\
                            \n{divisao_equilibrada(int(resultado), int(num))}'
                        )
                        break

                else:
                    print('Erro: operador inválido.')
                    continue

                if resultado.is_integer():
                    resultado = int(resultado)
                    os.system('cls')
                    print(f'\nResultado: {resultado}\n')

        elif entrada.lower() == 'p':
            print('\nPrograma encerrado.')
            break

        else:
            print('Erro: você não digitou nenhuma das opções.')

    except ValueError:
        print('Erro: valor inválido.')
        