ficha=list()
print('='*40)
print('{:^40}'.format('CADASTRO DE ALUNOS E NOTAS COM MÉDIA'))
print('='*40)   
while True:
    nome = str(input('\n Nome: '))
    nota1 = float(input(' Nota 1: '))
    nota2 = float(input(' Nota 2: '))
    nota3 = float(input(' Nota 3: '))
    nota4 = float(input(' Nota 4: '))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    ficha.append([nome, [nota1, nota2, nota3, nota4],media])
    resp=str(input('\nConinuar cadastro? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('='*40)
print(f'{"Nº":<4}{"NOME":<8}{"MÉDIA":>11}{"STATUS":>15}')
print('='*40)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<8}{a[2]:>10}',end='')
    if a[2] < 5:
        print(f'{"Reprovado":>17}')
    else:
        print(f'{"Aprovado":>17}')    
print('='*40)
while True:
    resp2=int(input('\nDigite o Nº do aluno para saber suas notas ou "999" para finalizar: '))
    if resp2 == 999:
        print('='*40)
        print(f'{"FIM... VOLTE SEMPRE!":^40}')
        print('='*40)
        break
    if resp2 <= len(ficha) -1:
        print(f'\nAs notas de {ficha[resp2][0]} são {ficha[resp2][1]}')
