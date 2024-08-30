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
        os.system('cls')

        if entrada.lower() == 'i':
            print('\nCalculadora v0.7.0\n')
            while True:
                try:
                    resultado = float(input('Primeiro número:\n'))
                    break  # Sai do loop se o valor for válido
                except ValueError:
                    os.system('cls')
                    print('\nErro: valor inválido. Tente novamente.\n')
            print()

            while True:
                operador = input('Operador (ou "F" para finalizar):\n')

                if operador.lower() == 'f':
                    break

                if operador in ['+', '-', '*', '/', '//', '**', '%', '%%']:
                    while True:
                        try:
                            num = float(input('\nPróximo número:\n'))
                            if num == 0:
                                if operador == '/' or operador == '//' \
                                    or operador == '%%':
                                    print('\nErro: divisão por zero.')
                                    continue
                            break  # Sai do loop se o valor for válido
                        except ValueError:
                            os.system('cls')
                            print('\nErro: valor inválido. Tente novamente.\n')

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
                                \n{divisao_equilibrada(
                                    int(resultado), int(num))}'
                        )
                        break

                    if resultado.is_integer():
                        resultado = int(resultado)

                    print(f'\nResultado: {resultado}\n')

                else:
                    print('\nErro: operador inválido.\n')

        elif entrada.lower() == 'p':
            print('\nPrograma encerrado.')
            break

        else:
            print('Erro: você não digitou nenhuma das opções.')

    except ValueError:
        os.system('cls')
        print('Erro: valor inválido.')