def calcula_atingimento(v, m):
    r = v / m
    return r * 100


for num in range(1, 4): # (1, 4) Quer dizer que ele começa no 1 e para antes do 4
    try:
        venda = float(input('informe o valor da venda: '))
        meta = float(input('informe o valor da meta: '))
        resultado = calcula_atingimento(venda, meta)
        # print(f'Resultado: {resultado}')
    except (ValueError, TypeError): # podem ser colocados juntos tipos de erros parecidos
        print('\n Digite apenas números seu animal...!!!')
    except ZeroDivisionError:
        print('\n A meta não pode ser zero')
        exit() # encerra a execução
    except KeyboardInterrupt:
        print('\n Interrompido pelo usuário')
    else:
        print(f'Resultado: {resultado}% da meta')
    finally:
        print('Operação Finalizada')