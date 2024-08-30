import os


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
            print('\nErro: valor inválido. Tente novamente.\n')


# Função para executar a operação matemática
def executar_operacao(numero, operador, prox_num):
    # Dicionário de operadores e suas funções correspondentes
    switch_operador = {
        '+': lambda: numero + prox_num,
        '-': lambda: numero - prox_num,
        '*': lambda: numero * prox_num,
        '/': lambda: numero / prox_num,
        '//': lambda: numero // prox_num,
        '**': lambda: numero ** prox_num,
        '%': lambda: numero % prox_num,
    }
    # Verifica se o operador está no dicionário e executa a operação
    if operador in switch_operador:
        return switch_operador[operador]()
    # Caso o operador seja '%%', executa a função da formula_brito
    elif operador == '%%':
        limpar_tela()
        print(f'Resultado:\n{divisao_equilibrada(int(numero), int(prox_num))}')
        main()


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
            '\nDigite "I" para iniciar a operação ou "P" para parar: ').lower()
        limpar_tela()

        # Inicia a operação
        if entrada == 'i':
            print('\nCalculadora v0.9.0\n')
            numero = obter_numero('Primeiro número:\n')

            while True:
                operador = input(
                    '\nOperador (ou "F" para finalizar):\n').lower()

                if operador == 'f':
                    break

                prox_num = obter_numero('\nPróximo número:\n')

                # Verifica se o próximo número (divisor) é zero em operações
                # que não permitem divisão por zero
                if prox_num == 0 and operador in ['/', '//', '%', '%%']:
                    print('\nErro: é impossível dividir por zero.')
                    continue

                # Executa a operação e atualiza o número
                resultado = executar_operacao(numero, operador, prox_num)
                if resultado is not None:
                    numero = int(resultado) if isinstance(
                        resultado, int) else resultado
                    print(f'\nResultado: {numero}\n')

        # Encerra o programa
        elif entrada == 'p':
            print('\nPrograma encerrado.')
            break

        else:
            print('Erro: você não digitou nenhuma das opções.')


# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
