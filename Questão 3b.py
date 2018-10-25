import random


def digito_igual(a, b):
    a = f'{a:0>3}'
    b = f'{b:0>3}'
    cont = 0
    if (len(a) or len(b)) > 3:
        return False
    else:
        for c in range(0, 3):
            if a[c] == b[0] or a[c] == b[1] or a[c] == b[2]:
                cont += 1
    return cont


n = random.randint(100, 999)
jg = None
tent = 5
for c in range(0, 6):
    jg = int(input('Digite um número de 100 a 999: '))
    if jg == n:
        print('Você acertou!')
        break
    else:
        if tent > 0:
            print(f'Você errou. Tem mais {tent} tentativas')
        else:
            print('Game Over!')
            print(f'O número escolhido foi {n}')
            break
        tent -= 1
        if jg > n:
            print('Tente um número menor!')
        else:
            print('Tente um número maior!')
        print(f'Seu palpite tem {digito_igual(jg, n)} dígitos iguais do número sorteado.')
    print()