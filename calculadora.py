import os
import sys

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


# Função para verificar se o número é inteiro ou float
def formatar(numero):
    if isinstance(numero, float) and numero.is_integer():
        return int(numero)
    return numero


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
        '%%': lambda: divisao_equilibrada(
            formatar(x), formatar(y), input(
                '\nNome e/ou separador (ou enter): ') or 'x', input(
                    'Nome 2 (ou enter): ')
                    ),
        '&': lambda: radiciacao(x, y)
    }

    try:
        if operador in switch_operador:
            resultado = switch_operador[operador]()
            # Verificação para evitar floats desnecessários
            resultado = formatar(resultado)
            # Adiciona a operação ao histórico
            historico.append((formatar(x), operador, formatar(y), resultado))
            return resultado

    except ZeroDivisionError:
        return '\nErro: é impossível dividir por zero.'


def divisao_equilibrada(dividendo, divisor, n1='x', n2=''):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    next = quociente + 1

    if resto == 0:
        return f'{quociente} {n1} {divisor} {n2}'

    if isinstance(dividendo, float) or isinstance(divisor, float):
        quociente = dividendo / divisor
        return f'{quociente} {n1} {divisor} {n2}'

    return f'\n{quociente} {n1} {(divisor
                                  - resto)} {n2}\n{next} {n1} {resto} {n2}'


# Função para radiciação
def radiciacao(x, y):
    potencia = 1 / y
    raiz = x ** potencia
    return raiz


# Função para exibir o histórico das operações
def exibir_historico():
    limpar_tela()
    print('\nHistórico das operações:')

    for i, operacao in enumerate(historico, 1):
        num_anterior, op, prox_num, resultado = operacao
        print(f'\n{i}. {num_anterior} {op} {prox_num} = {resultado}')


# Função para listar os comandos disponíveis
def lista_comandos():
    limpar_tela()
    print('Operadores disponíveis:')
    print(' +  : Adição')
    print(' -  : Subtração')
    print(' *  : Multiplicação x')
    print(' ** : Exponenciação ^')
    print(' /  : Divisão ÷')
    print(' // : Divisão inteira ÷')
    print(' %  : Módulo (resto) ÷')
    print(' %% : Divisão equilibrada ÷')
    print(' &  : Radiciação √ (1º número é o radicando e o próximo é o índice)')

    print('\nComandos disponíveis:')
    print(' L  : Exibir lista de operadores e comandos disponíveis')
    print(' H  : Histórico das operações')
    print(' R  : Resetar histórico')
    print(' F  : Finalizar operação (só funciona com o operador)')
    print(' P  : Parar o programa\n')


print('Calculadora v0.14.0')

operadores = ['+', '-', '*', '**', '/', '//', '%', '%%', '&']

# Lista para armazenar o histórico das operações
historico = []

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
            lista_comandos()
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
        