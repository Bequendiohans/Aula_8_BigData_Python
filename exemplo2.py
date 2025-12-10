alunos = []

for n in range(2):
    print(f'\n ----- Aluno {n+1} ------')
    nome = input('Infore o nome do aluno: ')

    notas = []
    for i in range(2):
        nota = float(input(f'Informe a nota {i+1}: '))
        notas.append(nota)
        
    media = sum(notas) / len(notas)

    aluno = {
        'Nome': nome,
        'Notas': notas,
        'Media': media
    }

    alunos.append(aluno)

#Exibindo os dados
for estudante in alunos:
    print(f'Nome: {estudante["Nome"]}')
    print(f'Notas: {estudante["Notas"]}')
    print(f'Media: {estudante["Media"]}\n')