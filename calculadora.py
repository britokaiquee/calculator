import sys
import os


############################ FUNÇÃO PRINCIPAL ##################################


def main():
    # Versão em que compilei pela primeira vez
    print('\nCalculadora v0.15.0 - by: Kaique.\n')
    print('"l" para listar operadores e comandos.\n\n')

    while True:
        # Solicita o primeiro número ou comando
        numero = obter_entrada('Primeiro número:\n')
        print()

        while True:
            operador = input('Operador:\n').lower()

            if processar_comando(operador):
                continue

            if operador == 'f':
                limpar_tela()
                print('"l" para listar operadores e comandos.\n')
                break

            operadores = ['+', '-', '*', '**', '/', '//', '%', '%%', '&']

            # Verifica se o operador é válido antes de continuar
            if operador not in operadores:
                limpar_tela()
                print('Operador ou comando inválido. Tente novamente.')
                print()
                continue

            # Solicita o próximo número ou comando
            print()
            prox_num = obter_entrada('Próximo número:\n')

            # Executa a operação e atualiza o número
            resultado = executar_operacao(numero, operador, prox_num)

            limpar_tela()
            print('L = listar operadores e comandos.\n')
            print(f'Resultado:\n{resultado}\n\n')

            if operador == '%%':
                break

            # Atualiza o número para a próxima iteração
            numero = resultado


################################ OPERAÇÃO ######################################


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
        '%%': lambda: resultado_div_e(x, y),
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
        return 'Impossível dividir por zero.\n'


def obter_entrada(mensagem):
    while True:
        entrada = input(mensagem).lower()
        if processar_comando(entrada):
            continue
        try:
            return float(entrada)
        except ValueError:
            limpar_tela()
            print('Valor ou comando inválido. Tente novamente.\n')


def formatar(numero):
    if isinstance(numero, float) and numero.is_integer():
        return int(numero)
    return numero


############################ OPERADORES CRIADOS ################################


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


def resultado_div_e(x, y):
    return divisao_equilibrada(
        formatar(x), formatar(y),
        input('\nNome e/ou separador (ou enter): ') or 'x',
        input('Nome 2 (ou enter): '))


# Raiz quadrada, cúbica, etc
def radiciacao(x, y):
    potencia = 1 / y
    raiz = x ** potencia
    return raiz


################################# COMANDOS #####################################


def processar_comando(comando):
    switch_comando = {
        'l': lista_comandos,
        'h': exibir_historico,
        'r': apagar_historico,
        'p': encerrar_calculadora,
    }
    if comando in switch_comando:
        switch_comando[comando]()
        return True
    return False


def lista_comandos():
    limpar_tela()
    print('Operadores disponíveis:')
    print(' +  : Adição')
    print(' -  : Subtração')
    print(' *  : Multiplicação x')
    print(' ** : Exponenciação ^')
    print(' /  : Divisão ÷')
    print(' // : Divisão inteira ÷')
    print(' %  : Módulo (resto da divisão) ÷')
    print(' %% : Divisão equilibrada ÷')
    print(' &  : Radiciação √ (1º número é o radicando e o próximo é o índice)')
    print('\nComandos disponíveis:')
    print(' l  : Exibir lista de operadores e comandos disponíveis')
    print(' h  : Histórico das operações')
    print(' r  : Resetar histórico')
    print(' f  : Finalizar operação (após ter enviado o 1º número)')
    print(' p  : Parar o programa\n\n')


# Lista para armazenar o histórico das operações
historico = []


def exibir_historico():
    limpar_tela()
    print('Histórico das operações:')
    for i, operacao in enumerate(historico, 1):
        num_anterior, op, prox_num, resultado = operacao
        print(f'{i}. {num_anterior} {op} {prox_num} = {resultado}\n')

    if not historico:
        print('Histórico vazio.\n')


def apagar_historico():
    if historico:
        historico.clear()
        limpar_tela()
        print('Histórico apagado.\n')
    else:
        limpar_tela()
        print('O histórico já está vazio.\n')


def encerrar_calculadora():
    limpar_tela()
    print('Programa encerrado.\n')
    sys.exit()


################################ OUTROS ########################################


# Função para limpar a tela, compatível com Windows e Unix-based OS
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
