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


print(digito_igual(1, 111))