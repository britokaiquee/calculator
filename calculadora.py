import os
import sys


print('Calculadora v0.12.0')

operadores = ['+', '-', '*', '**', '/', '//', '%', '%%']

# Lista para armazenar o histórico das operações
historico = []


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
def executar_operacao(x, operador, y):
    # Dicionário de operadores e suas funções correspondentes
    switch_operador = {
        '+': lambda: x + y,
        '-': lambda: x - y,
        '*': lambda: x * y,
        '**': lambda: x ** y,
        '/': lambda: x / y,
        '//': lambda: x // y,
        '%': lambda: x % y,
        '%%': lambda: divisao_equilibrada(int(x), int(y))
    }

    try:
        if operador in switch_operador:
            resultado = switch_operador[operador]()
            # Verificação para evitar floats desnecessários
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)
            # Adiciona a operação ao histórico
            historico.append((x, operador, y, resultado))
            return resultado

    except ZeroDivisionError:
        return '\nErro: é impossível dividir por zero.'


def divisao_equilibrada(dividendo, divisor, n1='x', n2=''):
    quociente = dividendo // divisor
    resto = dividendo % divisor

    if resto == 0:
        return f'{quociente} {n1} {divisor} {n2}'

    return f'{quociente} {n1} {(divisor - resto)} {n2}\n{(
        quociente + 1)} {n1} {resto} {n2}'


# Função para exibir o histórico das operações
def exibir_historico():
    limpar_tela()
    print('\nHistórico das operações:')

    for i, operacao in enumerate(historico, 1):
        num_anterior, op, prox_num, resultado = operacao

        # Formatação dos números para evitar floats desnecessários
        num_anterior = int(num_anterior) if isinstance(
            num_anterior, float) and num_anterior.is_integer() else num_anterior
        prox_num = int(prox_num) if isinstance(
            prox_num, float) and prox_num.is_integer() else prox_num
        resultado = int(resultado) if isinstance(
            resultado, float) and resultado.is_integer() else resultado

        print(f'{i}. {num_anterior} {op} {prox_num} = {resultado}')


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
            print(' H  : Histórico da operação')
            print(' R  : Resetar histórico')
            print(' F  : Finalizar operação')
            print(' P  : Parar/encerrar o programa')
            continue

        elif operador == 'p':
            limpar_tela()
            print('Programa encerrado.')
            sys.exit()

        elif operador == 'h':
            if not historico:
                limpar_tela()
                print('Histórico vazio.')
            else:
                exibir_historico()
            continue

        elif operador == 'r':
            limpar_tela()
            print('Histórico apagado.')
            historico = []
            continue

        # Verifica se o operador é válido antes de continuar
        if operador not in operadores:
            limpar_tela()
            print('\nOperador ou comando inválido. Tente novamente.')
            continue

        # Solicita o próximo número
        prox_num = obter_numero('\nPróximo número:\n')

        # Executa a operação e atualiza o número
        resultado = executar_operacao(numero, operador, prox_num)

        limpar_tela()
        print(f'Resultado:\n{resultado}')

        if operador == '%%':
            break

        # Atualiza o número para a próxima iteração
        numero = resultado