import os


# Função para limpar a tela, compatível com Windows e Unix-based OS
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


print('Calculadora v0.17.0\n')
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
        'L': listar_comandos,
        'H': exibir_historico,
        'A': apagar_historico,
        'D': divisao_equilibrada,
        'R': radiciacao
    }

    if comando in switch_comando:
        switch_comando[comando]()
        return True
    return False


def listar_comandos():
    limpar_tela()
    print('Calculadora criada por: Kaique Brito.')
    print('\n() | Use para agrupar expressões')
    print('\nOperadores:')
    print('+  | Adição')
    print('-  | Subtração')
    print('*  | Multiplicação')
    print('** | Exponenciação')
    print('/  | Divisão')
    print('// | Divisão inteira')
    print('#  | Módulo')
    print('\nOperadores bitwise (bit a bit):')
    print('&  | AND')
    print('|  | OR')
    print('^  | XOR')
    print('~  | NOT')
    print('<< | Deslocamento à esquerda')
    print('>> | Deslocamento à direita')
    print('\nOperadores especiais:')
    print('D  | Divisão equilibrada')
    print('R  | Radiciação (√)')
    print('P  | Porcentagem (%)')
    print('\nOutros comandos:')
    print('L  | Lista de operadores e comandos disponíveis')
    print('H  | Histórico das operações')
    print('A  | Apagar histórico')
    print('\nCtrl+c | Close\n')


############################### HISTÓRICO ######################################

# Lista para armazenar o histórico das operações
historico = []


def adicionar_historico(expressao, resultado):
    historico.append((expressao, resultado))


def exibir_historico():
    limpar_tela()
    print('Histórico das operações:')
    for i, (expressao, resultado) in enumerate(historico, 1):
        print(f'{i}| {expressao} = {resultado}')

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


########################### OPERADORES ESPECIAIS ###############################

# Fórmula pensada por mim, como uma variação da divisão inteira
def divisao_equilibrada():
    try:
        limpar_tela()
        dividendo = int(input('Dividendo: '))
        divisor = int(input('Divisor: '))
        quociente = dividendo // divisor
        resto = dividendo % divisor
        next = quociente + 1
        resultado = f'{quociente} x {divisor - resto} | {next} x {resto}'

        # guard clause pra retornar uma divisão inteira caso não haja resto
        if resto == 0:
            resultado = f'{quociente} x {divisor}'

        print(f'\nResultado:\n{resultado}\n')
        adicionar_historico(f'{dividendo} %% {divisor}', resultado)

    except ValueError:
        limpar_tela()
        print('Valor inválido.')

    except ZeroDivisionError:
        limpar_tela()
        print('Impossível dividir por zero.')


# Lógica para raiz quadrada, cúbica, etc...
def radiciacao():
    try:
        limpar_tela()
        indice = int(input('Índice: '))
        radicando = int(input('Radicando: '))
        potencia = 1 / indice
        raiz = radicando ** potencia
        resultado = formatar(raiz)
        print(f'\nResultado:\n{resultado}\n')
        adicionar_historico(f'(índice: {indice}) √{radicando}', resultado)

    except ValueError:
        limpar_tela()
        print('Valor inválido.')


################################################################################

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()