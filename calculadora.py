while True:
    try:
        entrada = input(
            '\nDigite "I" para iniciar a operação ou "P" para parar: ')
        if entrada == 'I' or entrada == 'i':
            print('\nCalculadora v0.1.0\n')
            num1 = int(input('Digite o primeiro número: '))
            operador = input('Digite o operador: ')
            num2 = int(input('Digite o segundo número: '))
            if operador == '+':
                print(f'A soma dos dois números é {num1+num2}')
            elif operador == '-':
                print(f'A subtração dos dois números é {num1-num2}')
            elif operador == '*':
                print(f'A multiplicação dos dois números é {num1*num2}')
            elif operador == '**':
                print(f'A exponenciação dos dois números é {num1**num2}')
            elif operador == '/':
                print(f'A divisão dos dois números é {num1/num2}')
            elif operador == '//':
                print(f'A divisão inteira dos dois números é {num1//num2}')
            elif operador == '%':
                print(f'O resto da divisão dos dois números é {num1%num2}')
            else:
                print('Erro: operador inválido.')
        elif entrada == 'P' or entrada == 'p':
            print('\nVocê saiu.')
            break
        else:
            print('Erro: você não digitou nenhuma das opções.')

    except:
        print('Erro: valor inválido.')