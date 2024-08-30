import re
import os
import textwrap
import tabulate
from tabulate import tabulate


################################ OPERAÇÃO ######################################

# Função principal
def entrada():
    print('Calculadora v0.23.0\n')
    print('Pressione "M" para ver o manual.\n')
    try:
        while True:
            # Solicita a expressão a ser avaliada
            expressao = input('\nDigite a expressão ou comando:\n').replace(
                ' ', '').upper()

            # Verifica a validade da expressão
            valido, mensagem = mensagem_erro(expressao)
            if not valido:
                limpar_tela()
                print(mensagem)
                continue

            if processar_comando(expressao):
                continue

            # Avalia a expressão e lida com possíveis erros
            try:
                resultado = resolver_expressao(expressao)
                limpar_tela()
                print(f'Resultado:\n{resultado}\n')
            except Exception:
                limpar_tela()
                print(f'Erro ao avaliar a expressão.\n')

    except KeyboardInterrupt:
        limpar_tela()


def verificar_expressao(expressao):
    # Verifica se há ponto no início ou no final da expressão
    if expressao.startswith('.') or expressao.endswith('.'):
        return False
    # Verifica se começa com um sinal de soma
    if expressao.startswith('+') or '(+' in expressao:
        return False
    # Verifica se não há operadores na expressão
    if expressao.isdigit() or '.' in expressao:
        # Remove todos os espaços e verifica se o restante é um número ou não
        expressao_limpa = expressao.replace('.', '').replace(' ', '')
        if expressao_limpa.isdigit():
            return False
    # Verifica se há apenas um número negativo
    if expressao.startswith('-'):
        if expressao.lstrip('-').isdigit():
            return False
    # Verifica se há um ou mais operadores consecutivos
    if '%%' in expressao or '++' in expressao or '--' in expressao:
        return False
    # Verifica se há a combinação do sinal de soma com o de subtração sem o uso
    # de parênteses
    if '-+' in expressao or '+-' in expressao:
        return False
    # Verifica se há ponto sem número à direita após operador
    if re.search(r'\.\D', expressao):
        return False
    # Verifica se há ponto sem número à esquerda antes do operador
    if re.search(r'\D\.', expressao):
        return False
    # Verifica se há parênteses que não foram fechados
    if expressao.count('(') != expressao.count(')'):
        return False
    # Verifica se há parênteses vazios
    if '()' in expressao:
        return False
    return True


def mensagem_erro(expressao):
    if not verificar_expressao(expressao):
        return False, "Erro: expressão mal formatada."
    return True, ""


def resolver_expressao(expressao):
    # Verifica se a expressão contém um operador válido
    if not re.search(r'[+\-*/#&|^~<<>>:@%()]', expressao):
        return 'Operador não encontrado. Verifique a expressão.'
    try:
        if ':' in expressao:
            return divisao_equilibrada(expressao)
        elif '@' in expressao:
            return radiciacao(expressao)
        elif '%' in expressao:
            return porcentagem(expressao)
        # Verifica se há apenas números e parênteses na expressão
        elif expressao.replace('(', '').replace(')', '').isdigit():
            resultado = 1
            for n in expressao.replace('(', '').replace(')', ''):
                resultado *= int(n)
            return resultado

        expressao = expressao.replace('#', '%')
        resultado = formatar(eval(expressao))
        adicionar_historico(expressao.replace('%', '#'), resultado)
        return resultado
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
    print('Observações sobre a radiciação e divisão equilibrada:')
    print('1. Digite o índice a direita do radical (representado por "@") e\
\no radicando a esquerda para calcular a raiz numa radiciação;')
    print('2. No momento não é possível realizar expressões de radiciação\
\nou divisão equilibrada envolvendo mais de um operador.\n')
    print('Observações sobre a porcentagem:')
    print('1. No momento só é possível fazer expressões básicas com porcentagem\
 (+-*/);')
    print('2. E também não é possível usar parênteses e números negativos em \
expressões\nde porcentagem com outros operadores.\n')
    print('Dicas:')
    print('1. É possível usar números negativos, parênteses e pontos para\
 números decimais;')
    print('2. Utilizar apenas números e parênteses resultará em uma\
 multiplicação;')
    print('3. É possível saber o percentual de uma porcentagem digitando \
números\n(inclusive negativos) com "%" no final, exemplo: "50%"\
 (resultado: 0.5);')
    print('4. Você pode saber a parte de um valor digitando a \
porcentagem seguida do valor\ntotal, exemplo: 5%20 (resultado: 1).\n')

    operadores = [
        ("+", "Adição"),
        ("-", "Subtração"),
        ("*", "Multiplicação"),
        ("**", "Exponenciação"),
        ("@", "Radiciação"),
        ("/", "Divisão"),
        ("//", "Divisão inteira"),
        (":", "Divisão equilibrada"),
        ("#", "Módulo (resto da divisão)"),
        ("%", "Porcentagem")
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
        ("M", "Manual"),
        ("H", "Histórico"),
        ("A", "Apagar histórico"),
        ("Ctrl+c", "Close (fechar programa)")
    ]

    print(tabulate(comandos,
                   headers=["Comandos:", "Descrição:"],
                   tablefmt="fancy_grid"))
    print('Para usar um comando, digite a letra uma vez e pressione Enter.\n')

    print(tabulate(operadores_logicos,
                   headers=["Operadores Bitwise (Bit-a-Bit):", "Descrição:"],
                   tablefmt="fancy_grid"))

    print()
    print(tabulate(operadores,
                   headers=["Operadores:", "Descrição:"],
                   tablefmt="fancy_grid"))

    print('\nArraste para cima para explorar mais o manual.\n')

# (possível comando para mostrar fórmulas dos operadores em breve...)


############################### HISTÓRICO ######################################

# Lista para armazenar o histórico das operações
historico = []


def adicionar_historico(expressao, resultado):
    historico.append((expressao, resultado))


def wrap(text, width):
    if not isinstance(text, str):
        text = str(text)  # Garantir que o texto seja uma string
    return "\n".join(textwrap.wrap(text, width))


def exibir_historico():
    limpar_tela()
    print('Histórico:')
    if historico:
        terminal_width = os.get_terminal_size().columns
        maxwidth = max(20, terminal_width // 3)

        tabelas = []
        for i, (expressao, resultado) in enumerate(historico, 1):
            tabelas.append([i, wrap(expressao, maxwidth), wrap(
                resultado, maxwidth)])

        headers = ["Expressão", "Resultado"]
        tabela = tabulate(tabelas, headers,
                          tablefmt="fancy_grid",
                          numalign="left")
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

    dividendo, divisor = map(int, expressao.split(':'))
    quociente = dividendo // divisor
    resto = dividendo % divisor
    next = quociente + 1
    resultado = f'{quociente} x {divisor - resto} | {next} x {resto}'

    # guard clause pra retornar uma divisão inteira caso não haja resto
    if resto == 0:
        resultado = f'{quociente} x {divisor}'

    adicionar_historico(f'{dividendo}:{divisor}', resultado)
    return resultado


# Lógica para raiz quadrada, cúbica, etc...
def radiciacao(expressao):
    limpar_tela()

    radicando, indice = map(int, expressao.split('@'))
    potencia = 1 / indice
    if radicando < 0:
        return '\nUse um número real.\n'
    else:
        # não pega o mesmo números de casas decimais que uma calculadora
        # científica
        raiz = formatar(radicando ** potencia)
        adicionar_historico(f'(índice: {indice}) √{radicando}', raiz)
        return raiz


def porcentagem(expressao):
    limpar_tela()

    while '%' in expressao:
        operador = re.search(r'[+\-*/]', expressao)
        match = re.search(r'(\d*\.?\d+)([+\-*/])(\d*\.?\d+)%', expressao)
        # Calcular valor com porcentagem do valor
        if operador and not expressao.startswith('-'):
            numero_antes = match.group(1)
            operador = match.group(2)
            porcentagem = match.group(3)

            # Construir a nova expressão substituindo a porcentagem
            nova_expressao = f'{numero_antes} {
                operador} ({numero_antes} * {porcentagem} / 100)'
            valor_final = expressao.replace(match.group(0), nova_expressao)
            break
        # Calcular percentual
        else:
            valor_final = re.sub(r'(\d+)%', r'(\1 / 100)', expressao)
            if re.search(r'%\d', expressao):
                porcentagem, valor = map(float, expressao.split('%'))
                valor_final = formatar((valor / 100) * porcentagem)
                adicionar_historico(expressao, valor_final)
                return valor_final
            break

    resultado = formatar(eval(valor_final))
    adicionar_historico(expressao, resultado)

    return resultado


################################################################################

# Função para limpar a tela, compatível com Windows e Unix-based OS
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    entrada()