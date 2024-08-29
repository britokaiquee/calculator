while True:
    try:
        entrada = input(
'\nDigite "I" para iniciar a operação ou "P" para parar, e pressione Enter. \n')
        if entrada == 'I' or entrada == 'i':
            print('\nCalculadora v0.2.0\n')
            num1 = float(input('Primeiro número:\n'))
            num2 = float(input('Segundo número:\n'))
            operador = input('Operador:\n')
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
            print(f'\nResultado = {resultado}')
        elif entrada == 'P' or entrada == 'p':
            print('\nVocê saiu.')
            break
        else:
            print('Erro: você não digitou nenhuma das opções.')
    except:
        print('Erro: valor inválido.')