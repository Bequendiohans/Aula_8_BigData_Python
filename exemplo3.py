def saudacao(n, i):
    print(f'Olá {n}, sua idade é {i}')


def soma(n1,n2):
    total = n1+n2 #sum(n1,n2)
    print(f'O resultado da soma destes números é: {total}.')


def maior_numero(a,b):
    if a > b:
        print(f'O maior é {a}')
    elif b > a:
        print(f'O maior é {b}')
    else:
        print('Os números são iguais.')


def somar_numeros(x,y):
    total = x + y
    total_final.append(total)

# nome = input('Informe o nome: ')
# idade = int(input('Informe a idade: '))
# saudacao(nome, idade)  #Para replicar o código da linha para baixo use: Shift + Alt + baixo(seta)

#-------------------------------------------- Programa Principal

# num1 = float(input('informe o primeiro número: '))
# num2 = float(input('Informe o segundo número: '))
# soma(num1, num2)

#----------------------------------------------- Descobre o maior

# numero1 = int(input('Informe o primeiro número: '))
# numero2 = int(input('Informe o segundo número: '))
# maior_numero (numero1, numero2)


total_final = []

for n in range(3):
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    somar_numeros(n1, n2)
   
print(total_final)