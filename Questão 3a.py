import random
n = random.randint(100, 999)
jg = None
tent = 5
for c in range(0, 6):
    jg = int(input('Digite um número de 100 a 999: '))
    if jg == n:
        print('Você acertou!')
        break
    else:
        if jg > n:
            print('Tente um número menor!')
        else:
            print('Tente um número maior!')
        if tent > 0:
            print(f'Você errou. Tem mais {tent} tentativas')
        else:
            print('Game Over!')
            print(f'O número escolhido foi {n}')
        tent -= 1
    print()