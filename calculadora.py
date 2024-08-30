while True:
    try:
        entrada = input(
            '\nDigite "I" para iniciar a operação ou "P" para parar: ')
        if entrada.lower() == 'i':
            print('\nCalculadora v0.3.0\n')
            num1 = float(input('Primeiro número:\n'))
            operador = input('Operador:\n')
            if operador in ['+', '-', '*', '/', '//', '**', '%']:
                num2 = float(input('Segundo número:\n'))
                if operador == '+':
                    resultado = num1 + num2
                elif operador == '-':
                    resultado = num1 - num2
                elif operador == '*':
                    resultado = num1 * num2
                elif operador == '/':
                    resultado = num1 / num2
                elif operador == '//':
                    resultado = num1 // num2
                elif operador == '**':
                    resultado = num1 ** num2
                elif operador == '%':
                    resultado = num1 % num2
                else:
                    print('Erro: operador inválido.')
                    continue

                # Se o resultado é um número inteiro, converta-o para int
                if resultado.is_integer():
                    resultado = int(resultado)
                print(f'\nResultado:\n{resultado}')
            else:
                print('Erro: operador inválido.')
        elif entrada.lower() == 'p':
            print('\nVocê saiu.')
            break
        else:
            print('Erro: você não digitou nenhuma das opções.')
    except ValueError:
        print('Erro: valor inválido.')
        