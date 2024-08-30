import re
import os
import textwrap
import tabulate
from tabulate import tabulate


################################ OPERAÇÃO ######################################

# Função principal
def entrada():
    print('Calculadora v0.21.0\n')
    print('Pressione "M" para ver o manual.\n')
    try:
        while True:
            # Solicita a expressão a ser avaliada
            expressao = input('\nDigite a expressão ou comando:\n').replace(
                ' ', '').upper()

            # Verifica a validade da expressão
            valido, mensagem = verificar_expressao(expressao)
            if not valido:
                limpar_tela()
                print(mensagem)
                continue

            if processar_comando(expressao):
                continue

            # Avalia a expressão e lida com possíveis erros
            try:
                resultado = avaliar_expressao(expressao)
                limpar_tela()
                print(f'Resultado:\n{resultado}\n')
            except Exception:
                limpar_tela()
                print(f'Erro ao avaliar a expressão. Tente novamente.\n')

    except KeyboardInterrupt:
        limpar_tela()


def verificar_ponto(expressao):
    # Verifica se há ponto no início ou no final da expressão
    if expressao.startswith('.') or expressao.endswith('.'):
        return False
    # Verifica se há ponto sem número à direita após operador
    if re.search(r'\.\D', expressao):
        return False
    # Verifica se há ponto sem número à esquerda antes do operador
    if re.search(r'\D\.', expressao):
        return False
    return True


def verificar_operador_no_inicio(expressao):
    # Verifica se a expressão começa com um operador
    return not re.match(r'[+\-*/#&|^~<<>>:@]', expressao)


def verificar_expressao(expressao):
    if not verificar_ponto(expressao):
        return False, "Expressão inválida: ponto mal posicionado."
    if not verificar_operador_no_inicio(expressao):
        return False, "Expressão inválida: não deve começar com um operador."
    return True, ""


def avaliar_expressao(expressao):
    # Verifica se a expressão contém um operador válido
    if not re.search(r'[+\-*/#&|^~<<>>:@]', expressao):
        return 'Operador não encontrado. Verifique a expressão.'

    # Verifica se a expressão contém o símbolo de porcentagem
    if '%' in expressao:
        return 'Use o comando "P" para expressões com porcentagem.'

    try:
        if ':' in expressao:
            return divisao_equilibrada(expressao)
        elif '@' in expressao:
            return radiciacao(expressao)

        expressao = expressao.replace('#', '%')
        resultado = eval(expressao)
        formatado = formatar(resultado)
        adicionar_historico(expressao, formatado)
        return formatado
    except ZeroDivisionError:
        return 'Impossível dividir por zero.\n'


def formatar(numero):
    if isinstance(numero, float) and numero.is_integer():
        return int(numero)
    return numero


################################# COMANDOS #####################################

def processar_comando(comando):
    switch_comando = {
        'M': exibir_manual,
        'P': porcentagem,
        # Comandos do histórico:
        'H': exibir_historico,
        'A': apagar_historico,
    }

    if comando in switch_comando:
        switch_comando[comando]()
        return True
    return False


def exibir_manual():
    limpar_tela()
    print('Calculadora e fórmula da divisão equilibrada\
\ncriadas por: Kaique Brito.\n')
    print('Obs 1: Digite o índice a esquerda do operador e o radicando a \
direita para radiciação.')
    print('Obs 2: No momento não é possível realizar expressões de radiciação \
envolvendo mais de um operador.\n')

    operadores = [
        ("+", "Adição"),
        ("-", "Subtração"),
        ("*", "Multiplicação"),
        ("**", "Exponenciação"),
        ("/", "Divisão"),
        ("//", "Divisão inteira"),
        ("#", "Módulo")
    ]

    operadores_logicos = [
        ("&", "AND"),
        ("|", "OR"),
        ("^", "XOR"),
        ("~", "NOT"),
        ("<<", "Deslocamento à esquerda"),
        (">>", "Deslocamento à direita")
    ]

    comandos = [
        ("P", "Porcentagem"),
        ("M", "Manual"),
        ("H", "Histórico"),
        ("A", "Apagar histórico"),
        ("Ctrl+c", "Close (fechar programa)")
    ]

    print('Para usar um comando, digite a letra uma vez e pressione Enter.\n')
    print(tabulate(comandos,
                   headers=["Comandos:", "Descrição:"],
                   tablefmt="fancy_grid"))

    print()
    print(tabulate(operadores_logicos,
                   headers=["Operadores Bitwise (Bit-a-Bit):", "Descrição:"],
                   tablefmt="fancy_grid"))

    print()
    print(tabulate(operadores,
                   headers=["Operadores:", "Descrição:"],
                   tablefmt="fancy_grid"))

    print('\nArraste para cima para explorar mais.\n')


############################### HISTÓRICO ######################################

# Lista para armazenar o histórico das operações
historico = []


def adicionar_historico(expressao, resultado):
    historico.append((expressao.replace('%', '#'), resultado))


def wrap(text, width):
    if not isinstance(text, str):
        text = str(text)  # Garantir que o texto seja uma string
    return "\n".join(textwrap.wrap(text, width))


def exibir_historico():
    limpar_tela()
    print('Histórico das operações:')
    if historico:
        terminal_width = os.get_terminal_size().columns
        maxwidth = max(20, terminal_width // 3)

        tabelas = []
        for i, (expressao, resultado) in enumerate(historico, 1):
            tabelas.append([i, wrap(expressao, maxwidth), wrap(
                resultado, maxwidth)])

        headers = ["Expressão", "Resultado"]
        tabela = tabulate(tabelas, headers, tablefmt="fancy_grid")
        print(tabela)
    else:
        print('Histórico vazio.\n')


def apagar_historico():
    if historico:
        historico.clear()
        limpar_tela()
        print('Histórico apagado.\n')
    else:
        limpar_tela()
        print('O histórico já está vazio.\n')


########################### OPERADORES ESPECIAIS ###############################

# Fórmula pensada por mim, como uma variação da divisão inteira
def divisao_equilibrada(expressao):
    limpar_tela()
    try:
        dividendo, divisor = map(int, expressao.split(':'))
        quociente = dividendo // divisor
        resto = dividendo % divisor
        next = quociente + 1
        resultado = f'{quociente} x {divisor - resto}\n{next} x {resto}'

        # guard clause pra retornar uma divisão inteira caso não haja resto
        if resto == 0:
            resultado = f'{quociente} x {divisor}'

        adicionar_historico(f'{dividendo}:{divisor}', resultado)
        return resultado

    except ValueError:
        return 'Não é possível usar mais de um operador\
\ncom o de divisão equilibrada.'

    except ZeroDivisionError:
        return 'Impossível dividir por zero.'


# Lógica para raiz quadrada, cúbica, etc...
def radiciacao(expressao):
    limpar_tela()
    try:
        indice, radicando = map(int, expressao.split('@'))
        potencia = 1 / indice

        # Verifica se o radicando é negativo
        if radicando < 0:
            return '\nUse um número real.\n'
        else:
            raiz = formatar(radicando ** potencia)
            adicionar_historico(f'(índice: {indice}) √{radicando}', raiz)
            return raiz

    except ValueError:
        return 'Desculpe, não consigo realizar expressões envolvendo\
\nradiciação e outros operadores no momento.'


def porcentagem():
    limpar_tela()
    print('Porcentagem')
    print('Enter = saber o valor da porcentagem sem realizar cálculo.\n')
    try:
        valor_total = float(input('Valor: '))
        operador = input('Operador ou Enter: ')
        porcentagem = float(input('Porcentagem %: '))
        parte_valor = (valor_total / 100) * porcentagem

        if operador == '':
            resultado = formatar(parte_valor)
            print(f'\nResultado: {resultado}\n')
            expressao = f'{formatar(porcentagem)}% de {formatar(valor_total)}'

        else:
            calculo = f'{valor_total}{operador}{parte_valor}'
            resultado = formatar(eval(calculo))
            print(f'\nResultado: {resultado}\n')
            expressao = f'{formatar(valor_total)}{operador}{formatar(
                porcentagem)}%'

        adicionar_historico(expressao, resultado)

    except ValueError:
        print('\nErro: valor inválido.\n')

    except SyntaxError:
        print('\nErro: operador inválido.\n')


################################################################################

# Função para limpar a tela, compatível com Windows e Unix-based OS
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    entrada()
