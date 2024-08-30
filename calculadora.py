while True:
    try:
        entrada = input(
            '\nDigite "I" para iniciar a operação ou "P" para parar: ')
        if entrada.lower() == 'i':
            print('\nCalculadora v0.4.0\n')
            resultado = float(input('Primeiro número:\n'))
            while True:
                operador = input(
                    'Operador (ou "R" para mostrar o resultado):\n')
                if operador.lower() == 'r':
                    break
                if operador in ['+', '-', '*', '/', '//', '**', '%']:
                    num = float(input('Próximo número:\n'))
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
                else:
                    print('Erro: operador inválido.')
                    continue

            if resultado.is_integer():
                resultado = int(resultado)
            print(f'\nResultado:\n{resultado}')
        elif entrada.lower() == 'p':
            print('\nVocê saiu.')
            break
        else:
            print('Erro: você não digitou nenhuma das opções.')
    except ValueError:
        print('Erro: valor inválido.')
