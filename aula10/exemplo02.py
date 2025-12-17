
lst_vendas = []
resposta = 's'
venda = 1
tentativa = 1

while resposta != 'n':
    try:
        valor = float(input(f'Informe o valor da {venda}ª venda: '))
    except (ValueError, TypeError):
        print('\nInforme apenas números')
    except KeyboardInterrupt:
        print('\nEncerrado pelo usuário')
        break
    else:
        lst_vendas.append(valor)
        resposta = input(f'Deseja continuar [s/n]? ')[0].lower()
        venda += 1
    finally:
        print(f'Tentativa {tentativa} \n')
        tentativa += 1

print(f'Vendas registradas {lst_vendas}')