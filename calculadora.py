import os
from tabulate import tabulate


# Função para limpar a tela, compatível com Windows e Unix-based OS
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


print('Calculadora v0.19.0\n')
print('Pressione "L" para listar\noperadores e comandos.\n')


################################ OPERAÇÃO ######################################

# Função principal
def main():
    try:
        while True:
            # Solicita a expressão a ser avaliada
            expressao = input('\nDigite a expressão ou comando:\n').replace(
                ' ', '').upper()
            if processar_comando(expressao):
                continue
            # Verifica se a expressão contém o símbolo de porcentagem
            if '%' in expressao:
                limpar_tela()
                print('Use o comando "P" para expressões com porcentagem.')
                continue

            # Avalia a expressão e lida com possíveis erros
            try:
                resultado = avaliar_expressao(expressao)
                limpar_tela()
                print('L = listar operadores e comandos.\n')
                print(f'Resultado:\n{resultado}\n')
            except Exception:
                limpar_tela()
                print(f'Erro ao avaliar a expressão. Tente novamente.')

    except KeyboardInterrupt:
        limpar_tela()


def avaliar_expressao(expressao):
    try:
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
        'L': exibir_lista,
        # Comandos do histórico:
        'H': exibir_historico,
        'A': apagar_historico,
        # Comandos dos operadores especiais:
        'D': divisao_equilibrada,
        'R': radiciacao,
        'P': porcentagem
    }

    if comando in switch_comando:
        switch_comando[comando]()
        return True
    return False


def exibir_lista():
    limpar_tela()
    print('Calculadora criada por: Kaique Brito.')

    operadores = [
        ("+", "Adição", "&", "AND", "D", "(:) Divisão equilibrada"),
        ("-", "Subtração", "|", "OR", "R", "(√) Radiciação"),
        ("*", "Multiplicação", "^", "XOR", "P", "(%) Porcentagem"),
        ("**", "Exponenciação", "~", "NOT", "L", "Listar"),
        ("/", "Divisão", "<<", "Deslocamento à esquerda", "H", "Histórico"),
        ("//", "Divisão inteira", ">>", "Deslocamento à direita", "A",
         "Apagar histórico"),
        ("#", "Módulo", "", "", "Ctrl+c", "Close")
    ]

    print(tabulate(operadores,
                   headers=["Operadores:", "Descrição:",
                            "Operadores bitwise\n(bit a bit):", "Descrição:",
                            "Outros operadores e comandos:", "Descrição:"],
                   tablefmt="fancy_grid"))


############################### HISTÓRICO ######################################

# Lista para armazenar o histórico das operações
historico = []


def adicionar_historico(expressao, resultado):
    historico.append((expressao.replace('%', '#'), resultado))


def exibir_historico():
    limpar_tela()
    print('Histórico das operações:')

    if historico:
        tabelas = []
        for i, (expressao, resultado) in enumerate(historico, 1):
            tabelas.append([i, expressao, resultado])

        headers = ["Index", "Expressão", "Resultado"]
        tabela = tabulate(tabelas, headers,
                          tablefmt="fancy_grid",
                          numalign="center",
                          stralign="center")
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
def divisao_equilibrada():
    limpar_tela()
    print('Divisão equilibrada\n')

    try:
        dividendo = int(input('Dividendo: '))
        divisor = int(input('Divisor: '))
        quociente = dividendo // divisor
        resto = dividendo % divisor
        next = quociente + 1
        resultado = f'{quociente} x {divisor - resto}\n{next} x {resto}'

        # guard clause pra retornar uma divisão inteira caso não haja resto
        if resto == 0:
            resultado = f'{quociente} x {divisor}'

        print(f'\nResultado:\n{resultado}\n')
        adicionar_historico(f'{dividendo}:{divisor}', resultado)

    except ValueError:
        print('Valor inválido.')

    except ZeroDivisionError:
        print('Impossível dividir por zero.')


# Lógica para raiz quadrada, cúbica, etc...
def radiciacao():
    print('Radiciação\n')
    limpar_tela()

    try:
        indice = int(input('Índice: '))
        radicando = int(input('Radicando: '))
        potencia = 1 / indice

        # Verifica se o radicando é negativo
        if radicando < 0:
            print("\nUse um número real.\n")
        else:
            raiz = formatar(radicando ** potencia)
            print(f'\nResultado:\n{raiz}\n')
            adicionar_historico(f'(índice: {indice}) √{radicando}', raiz)

    except ValueError:
        print('\nValor inválido.\n')


def porcentagem():
    limpar_tela()
    print('Porcentagem\n')

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
        print('\nValor inválido.\n')

    except SyntaxError:
        print('\nOperador inválido.\n')


################################################################################

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
