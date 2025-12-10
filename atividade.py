# DICIONÁRIOS E LISTAS (VENDAS)

vendedores = []

for n in range(3):
    print(f'Vendedor {n+1}: ')
    nome = input('Infome seu nome: ')

    vendas = []
    for v in range(5):
        venda = float(input(f'Informe o valor da venda {v+1}: '))
        vendas.append(venda)
        total = sum(vendas)
        media = sum(vendas) / len(vendas)
    
    vendedor = {
        'Nome': nome,
        'Vendas':vendas,
        'Total': total,
        'Media': media,
    }
    vendedores.append(vendedor)

for cadastro in vendedores:
    print(cadastro)