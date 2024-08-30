while True:
    try:
        entrada = input(
            '\nDigite "I" para iniciar a operação ou "P" para parar: ')
        if entrada.lower() == 'i':
            print('\nCalculadora v0.5.0\n')
            resultado = float(input('Primeiro número:\n'))
            while True:
                if resultado.is_integer():
                    resultado = int(resultado)
                print(f'\nResultado total: {resultado}')
                operador = input(
                    'Operador (ou "F" para finalizar):\n')
                if operador.lower() == 'f':
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

        elif entrada.lower() == 'p':
            print('\nPrograma encerrado.')
            break
        else:
            print('Erro: você não digitou nenhuma das opções.')
    except ValueError:
        print('Erro: valor inválido.')
