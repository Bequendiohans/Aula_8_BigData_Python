#ATIVIDADE 01

def valor_total(v,q):
    t = v * q
    #print(f'Valor total:R${t}')
    return t


for v in range(3):
    venda = float(input('Informe o valor do produto: '))
    qtd = int(input('Informe a quantidade do produto: '))
    total = valor_total(venda, qtd)
    print(f'Valor total:R${total}')


