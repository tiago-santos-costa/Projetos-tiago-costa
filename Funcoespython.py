def metade(n):
    print('-'*35)
    res = n / 2
    return f'A metade de R${n:.2f} é R${res:.2f}'.replace('.',',')


def dobro(n):
    print('-'*35)
    res = n * 2
    return f'O dobro de R${n:.2f} é R${res:.2f}'.replace('.',',')
    

def aumentar(n, taxa):
    print('-'*35)
    resp = ((taxa * n) / 100) + n
    return f'Aumentando {taxa}%, temos R$R${resp:.2f}'.replace('.',',')
    

def diminuir(n, taxa):
    print('-'*35)
    resp = n - ((taxa * n) / 100)
    return f'Dinuindo {taxa}%, temos R$R${resp:.2f}'.replace('.',',')


def parouímpar(n):
    print('-'*35)
    if n %2==0:
       return f'O número {n:.0f} é PAR'
    else:
        return f'O número {n:.0f} é ÍMPAR'
 

def fatorial(n):
    print('-'*35)
    f = 1
    for c in range(1, n +1 ):
        f=f*c
    return f'O fatorial de {n} é {f}'


def quantosPares(n):
    print('-'*50)
    print('PARES', end=' -> ')
    cont=soma=0
    for c in range(0, n +1):
        if c %2==0:
            cont+=1
            soma = soma + c
            media = soma / cont
            print(f'{c}',end=' ')
    return f'(Totalizando {cont} números PARES) que somados resultam em {soma}\n- Média dos PARES {media}'

    
def quantosímpar(n):
    print('-'*50)
    print("ÍMPARES", end=' -> ')
    cont = soma = media = 0
    for c in range(0, n +1):
        if c %2==1:
            cont+=1
            soma = soma + c
            media = soma / cont
            print(f'{c}',end=' ')       
    return f'(Totalizando {cont} números ÍMPARES) que somados resultam em {soma}\n- Média dos ÍMPARES {media}'
    

def leiaInt(numero):
    while True:
        try:
            n = int(input(numero))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n
    

def leiaFloat(numero):
    while True:
        try:
            n = float(input('Digite um número real: '))
        except (TypeError, ValueError):
            print('\033[31mERRO! Por favor digite um número Real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar')
            return 0
        else:
            return n


p = int(input('\nDigite um preço: R$'))
print(metade(p))
print(dobro(p))
print(aumentar(p, 20))
print(diminuir(p, 32))
print(parouímpar(p))
print(fatorial(p))
print(quantosPares(p))
print(quantosímpar(p))
print('\nFIM')