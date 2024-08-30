import os
import sys


print('Calculadora v0.11.0')

operadores = ['+', '-', '*', '**', '/', '//', '%', '%%']


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
        '%%': lambda: divisao_equilibrada(int(numero), int(prox_num))
    }

    try:
        if operador in switch_operador:
            return switch_operador[operador]()

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
        # Solicita o primeiro número
        numero = obter_numero('\nPrimeiro número:\n')

        while True:
            operador = input('\nOperador/comando ("L" para listar):\n').lower()

            if operador == 'f':
                limpar_tela()
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

                print('\nComandos disponíveis:')
                print(' L  : Exibir lista de operadores e comandos disponíveis')
                print(' F  : Finalizar operação')
                print(' P  : Parar/encerrar o programa')
                continue

            elif operador == 'p':
                limpar_tela()
                print('Programa encerrado.')
                sys.exit()

            # Verifica se o operador é válido antes de continuar
            if operador not in operadores:
                limpar_tela()
                print('\nOperador ou comando inválido. Tente novamente.')
                continue

            # Solicita o próximo número
            prox_num = obter_numero('\nPróximo número:\n')

            # Executa a operação e atualiza o número
            resultado = executar_operacao(numero, operador, prox_num)

            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)

            limpar_tela()
            print(f'Resultado:\n{resultado}')

            if operador == '%%':
                break

            # Atualiza o número para a próxima iteração
            numero = resultado

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()