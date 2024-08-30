import os


# Função para limpar a tela, compatível com Windows e Unix-based OS
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# Função principal
def main():
    try:
        print('Calculadora v0.16.0 - by: Kaique.\n')
        print('"l" para listar operadores e comandos.\n\n')

        while True:
            # Solicita o primeiro número ou comando
            numero = obter_entrada('Primeiro número:\n')
            print()

            while True:
                operador = input('Operador:\n').lower()

                if processar_comando(operador):
                    continue

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
                print('Pressione "l" para listar operadores e comandos.\n')
                print(f'Resultado:\n{resultado}\n\n')

                if operador == '%%':
                    break

                # Atualiza o número para a próxima iteração
                numero = resultado

    except KeyboardInterrupt:
        limpar_tela()

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
        '%%': lambda: divisao_equilibrada(formatar(x), formatar(y)),
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

# Fórmula criada por mim
def divisao_equilibrada(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    next = quociente + 1
    
    # guard clause pra retornar uma divisão inteira caso não haja resto
    if resto == 0:
        return f'{quociente} x {divisor}'

    # guard clause pra retornar uma divisão normal caso haja números flutuantes
    if isinstance(dividendo, float) or isinstance(divisor, float):
        quociente = dividendo / divisor
        return f'{quociente} x {divisor}'

    return f'\n{quociente} x {(divisor - resto)}\n{next} x {resto}'


# Raiz quadrada, cúbica, etc
def radiciacao(x, y):
    potencia = 1 / y
    raiz = x ** potencia
    return raiz

################################# COMANDOS #####################################

def processar_comando(comando):
    switch_comando = {
        'l': listar_comandos,
        'h': exibir_historico,
        'a': apagar_historico,
        'r': reiniciar_calculadora,
    }

    if comando in switch_comando:
        switch_comando[comando]()
        return True
    return False


def listar_comandos():
    limpar_tela()
    print('Operadores disponíveis:')
    print('+  | Adição')
    print('-  | Subtração')
    print('*  | Multiplicação x')
    print('** | Exponenciação ^')
    print('/  | Divisão ÷')
    print('// | Divisão inteira ÷')
    print('%  | Módulo (resto da divisão) ÷')
    print('%% | Divisão equilibrada ÷')
    print('&  | Radiciação √ (1º número é o radicando e o próximo é o índice)')
    print('\nObs: o primeiro número passa a ser o resultado após a 1ª conta,')
    print('mas você pode usar o comando "r" pra resetar.')
    print('\nComandos disponíveis:')
    print('l  | Lista de operadores e comandos disponíveis')
    print('h  | Histórico das operações')
    print('a  | Apagar histórico')
    print('r  | Reiniciar calculadora (finalizar operação)')
    print('\nCtrl+c | Close\n\n')


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


def reiniciar_calculadora():
    limpar_tela()
    main()

################################################################################

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
