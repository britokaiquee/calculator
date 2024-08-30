import os

print('\nCalculadora v0.10.0')

# Função para limpar a tela, compatível com Windows e Unix-based OS
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# Função para obter um número do usuário com tratamento de erro
def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            limpar_tela()
            print('\nValor inválido. Tente novamente.')


# Função para executar a operação matemática
def executar_operacao(numero, operador, prox_num):
    # Dicionário de operadores e suas funções correspondentes
    switch_operador = {
        '+': lambda: numero + prox_num,
        '-': lambda: numero - prox_num,
        '*': lambda: numero * prox_num,
        '**': lambda: numero ** prox_num,
        '/': lambda: numero / prox_num,
        '//': lambda: numero // prox_num,
        '%': lambda: numero % prox_num,
    }

    try:
        if operador in switch_operador:
            return switch_operador[operador]()
        elif operador == '%%':
            limpar_tela()
            print(f'Resultado:\n{divisao_equilibrada(
                int(numero), int(prox_num))}')
            main()
        else:
            return 'Operador inválido'

    except ZeroDivisionError:
        return '\nErro: é impossível dividir por zero.'


def divisao_equilibrada(dividendo, divisor, n1='x', n2=''):
    quociente = dividendo // divisor
    resto = dividendo % divisor

    if resto == 0:
        return f'{quociente} {n1} {divisor} {n2}'

    return f'{quociente} {n1} {(divisor - resto)} {n2}\n{(
        quociente + 1)} {n1} {resto} {n2}'


# Função principal que controla o fluxo do programa
def main():
    while True:
        # Solicita ao usuário para iniciar ou parar a operação
        entrada = input(
            '\nDigite "C" para continuar ou "P" para parar: ').lower()
        limpar_tela()

        # Inicia a operação
        if entrada == 'c':
            numero = obter_numero('\nPrimeiro número:\n')

            while True:
                operador = input('\nOperador ou comando ("F" para finalizar \
| "L" para listar operadores):\n').lower()

                if operador == 'f':
                    break
                elif operador == 'l':
                    limpar_tela()
                    print('\nOperadores disponíveis:')
                    print(' +  : Adição')
                    print(' -  : Subtração')
                    print(' *  : Multiplicação')
                    print(' ** : Exponenciação')
                    print(' /  : Divisão')
                    print(' // : Divisão inteira')
                    print(' %  : Módulo')
                    print(' %% : Divisão equilibrada')
                    continue

                # Verifica se o operador é válido antes de continuar
                if operador not in ['+', '-', '*', '**', '/', '//', '%', '%%']:
                    limpar_tela()
                    print('\nOperador inválido. Tente novamente.')
                    continue

                prox_num = obter_numero('\nPróximo número:\n')

                # Executa a operação e atualiza o número
                resultado = executar_operacao(numero, operador, prox_num)

                if isinstance(resultado, float) and resultado.is_integer():
                    resultado = int(resultado)

                print(f'\nResultado: {resultado}\n')

                # Atualiza o número para a próxima iteração
                numero = resultado

        # Encerra o programa
        elif entrada == 'p':
            print('\nPrograma encerrado.')
            break

        else:
            print('Erro: você não digitou nenhuma das opções.')


# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
