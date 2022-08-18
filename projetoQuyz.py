print('\n>>>>>>>>>> BEM VINDO AO QUIZ DO CHAVES <<<<<<<<<<\n')
usuario=input('Vamos começar? s/n:')
resposta='S'

while resposta == 'S':
    
    score = 0

    if usuario != 's':
        quit()

    print(  '\nComeçando ...\n')
    print('Quantos meses de aluguel seu Madruga deve ao Sr. Barriga? \n\n (a) 13 meses \n (b) 10 meses \n (c) 14 meses \n (d) 9 meses \n')
    usuario1=input('Resposta:')

    if usuario1 == 'c':
        print('\n              Parabéns!\n')
        score = score + 1

    else:
        print('\n              Escolha errada :(\n')

    print('Qual era o verdadeiro nome do Chaves? \n\n (a) Chespirito \n (b) Roberto Gómez Bolaños \n (c) Carlos Villagrán \n (d) Ramón Valdés \n')
    usuario2=input('Resposta:')

    if usuario2 == 'b':
        print('\n              Parabéns!\n')
        score = score + 1
    else:
        print('\n              Escolha errada :(\n')

    print('Qual é o nome completo de Sr. Barriga? \n\n (a) Zenon Cachalote \n (b) Zenon Barriga e Pesado \n (c) Zenon Pesado e Barriga \n (d) Zenon Dom Barriga e Pesado \n')
    usuario2=input('Resposta:')

    if usuario2 == 'b':
        print('\n              Parabéns!\n')
        score = score + 1
    else:
        print('\n              Escolha errada :(\n')

    print('De quem Seu Madruga é pai? \n\n (a) paty \n (b) kiko \n (c) Chiquinha \n (d) Pópis \n')
    usuario2=input('Resposta:')

    if usuario2 == 'c':
        print('\n              Parabéns!\n')
        score = score + 1
    else:
        print('\n              Escolha errada :(\n')

    print('De quem é a frase "prefiro morrer do que perder a vida"? \n\n (a) Seu Madruga \n (b) Chiquinha \n (c) Kiko \n (d) Chaves \n')
    usuario3=input('Resposta:')

    if usuario3 == 'd':
        print('\n              Parabéns!\n')
        score = score + 1
    else:
        print('\n              Escolha errada :(\n')

    print('Quem interpretou Professor Girafales? \n\n (a) Rubén Aguirre \n (b) Ramón Valdez \n (c) Carlos Villagran \n (d) Edgar Vivar \n')
    usuario2=input('Resposta:')

    if usuario2 == 'a':
        print('\n              Parabéns!\n')
        score = score + 1
    else:
        print('\n              Escolha errada :(\n')
        
    print('No episódio do festival da boa vizinhança, quem conta a história do cão arrependido? \n\n (a) Chaves \n (b) Kiko \n (c) Chiquinha \n (d) Seu Madruga \n')
    usuario2=input('Resposta:')

    if usuario2 == 'a':
        print('\n              Parabéns!\n')
        score = score + 1
    else:
        print('\n              Escolha errada :(\n')

    print('Quem leva Chaves para Acapulco? \n\n (a) Prof. Girafales \n (b) A bruxa do 71 \n (c) Seu Madruga \n (d) Sr. Barriga \n')
    usuario2=input('Resposta:')

    if usuario2 == 'd':
        print('\n           Parabéns!\n')
        score = score + 1
    else:
        print('\n              Escolha errada :(\n')

    if score == 8:
        print('Parabén pontuação máxima!')

    
    print('  Total de pontos: {} (de 8 possíveis)  \n\nQuiz acabou :)\n'.format(score))
    resposta=str(input('Jogar novamente? ')).upper().strip()[0]
print('\n      FIM')
