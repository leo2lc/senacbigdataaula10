# Atividade 01
# VsCode - GitHub

# Crie um programa em Python que receba 3 pares de números e faça a soma de cada par mostrando o resultado

# Requisitos: funções, laço de repetição e tratamento de Exceções

# O programa deve: 
# Solicitar dois valores ao usuário
# somar os valores
# repetir a operação 3 vezes
# tratar possíveis erros de entrada com try/except
# Exibir o resultado da soma quando não houver erro.

def soma(n1, n2):
    tt = n1 + n2
    return tt

valores = []

for n in range(1, 4):
    try:
        num1 = int(input('Insira o 1º valor: '))
        num2 = int(input('Insira o 2º valor: '))
        total = soma(num1, num2)
    except(ValueError, TypeError):
        print('\n Digite apenas números')
    else:
        print(f'O total é: {total}')
        valores.append(total)
print(valores)
