from time import sleep
print('='*50)
print(f'\n{"> > > > BEM VINDO AO QUIZ DO CHAVES < < < <":^50}\n')
print('='*50)

while True:
    score=0
    resposta=str(input('Podemos começar? [S/N] ')).upper()
    if resposta == 'N':
        break 

    print('\nComeçando',end='',flush=True) 
    sleep(0.5)
    print('.',end='',flush=True)
    sleep(0.5)
    print('.',end='',flush=True)
    sleep(0.5)
    print('.',flush=True)
    sleep(0.5)

    print('\n1) Quantos meses de aluguel seu Madruga deve ao Sr. Barriga?\n'.upper(), '(a) 13 meses \n (b) 10 meses \n (c) 14 meses \n (d) 9 meses \n')
    resposta=str(input('Digite a letra correspondente: ')).upper().strip()
    if resposta == 'C':
        score+=1
        print(f'\n{"PARABÉNS! Alternativa correta.":^40}')
    else:
        print(f'\n{":( Resposta errada":^40}')
    sleep(0.5)

    print('\n2) Qual é o nome completo de Sr. Barriga?\n'.upper(), '(a) Zenon Cachalote \n (b) Zenon Barriga e Pesado \n (c) Zenon Pesado e Barriga \n (d) Zenon Dom Barriga e Pesado \n')
    resposta=str(input('Digite a letra correspondente: ')).upper().strip()
    if resposta == 'B':
        score+=1
        print(f'\n{"PARABÉNS! Alternativa correta.":^40}')
    else:
        print(f'\n{":( Resposta errada":^40}')   
    sleep(0.5)

    print('\n3) De quem Seu Madruga é pai?\n'.upper(), '(a) paty \n (b) kiko \n (c) Chiquinha \n (d) Pópis \n')
    resposta=str(input('Digite a letra correspondente: ')).upper().strip()
    if resposta == 'C':
        score+=1
        print(f'\n{"PARABÉNS! Alternativa correta.":^40}')
    else:
        print(f'\n{":( Resposta errada":^40}')   
    sleep(0.5)

    print('\n4) De quem é a frase "prefiro morrer do que perder a vida"?\n'.upper(), '(a) Seu Madruga \n (b) Chiquinha \n (c) Kiko \n (d) Chaves \n')
    resposta=str(input('Digite a letra correspondente: ')).upper().strip()
    if resposta == 'D':
        score+=1
        print(f'\n{"PARABÉNS! Alternativa correta.":^40}')
    else:
        print(f'\n{":( Resposta errada":^40}')   
    sleep(0.5)

    print('\n5) Quem interpretou Professor Girafales?\n'.upper(), '(a) Rubén Aguirre \n (b) Ramón Valdez \n (c) Carlos Villagran \n (d) Edgar Vivar \n')
    resposta=str(input('Digite a letra correspondente: ')).upper().strip()
    if resposta == 'A':
        score+=1
        print(f'\n{"PARABÉNS! Alternativa correta.":^40}')
    else:
        print(f'\n{":( Resposta errada":^40}')   
    sleep(0.5)

    print('\n6) No episódio do festival da boa vizinhança, quem conta a história do cão arrependido?\n'.upper(), '(a) Chaves \n (b) Kiko \n (c) Chiquinha \n (d) Seu Madruga \n')
    resposta=str(input('Digite a letra correspondente: ')).upper().strip()
    if resposta == 'A':
        score+=1
        print(f'\n{"PARABÉNS! Alternativa correta.":^40}')
    else:
        print(f'\n{":( Resposta errada":^40}')   
    sleep(0.5)

    print('\n7) Quem leva Chaves para Acapulco?\n'.upper(), '(a) Prof. Girafales \n (b) A bruxa do 71 \n (c) Seu Madruga \n (d) Sr. Barriga \n')
    resposta=str(input('Digite a letra correspondente: ')).upper().strip()
    if resposta == 'D':
        score+=1
        print(f'\n{"PARABÉNS! Alternativa correta.":^40}')
    else:
        print(f'\n{":( Resposta errada":^40}')   
    sleep(0.5)

    print('\n8) Qual era o verdadeiro nome do Chaves?\n'.upper(), '(a) Chespirito \n (b) Roberto Gómez Bolaños \n (c) Carlos Villagrán \n (d) Ramón Valdés \n')
    resposta=str(input('Digite a letra correspondente: ')).upper().strip()
    if resposta == 'B':
        score+=1
        print(f'\n{"PARABÉNS! Alternativa correta.":^40}')
    else:
        print(f'\n{":( Resposta errada":^40}')   
    sleep(0.5)

    if score == 8:
        print('\n    Parabén pontuação máxima!'.upper())
    print(f'  Total de pontos: {score} (de 8 possíveis)  \n\nQuiz acabou :)\n')

    resposta=str(input('\nJogar novamente? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print('='*20)
print('    VOLTE SEMPRE ')
print('='*20)