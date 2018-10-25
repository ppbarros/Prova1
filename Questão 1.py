def isinverse(a, b):
    a = str(a)
    b = str(b)
    ca = 0
    cb = len(b) - 1
    if len(a) != len(b):
        return False
    while True:
        if a[ca] != b[cb]:
            return False
        else:
            if ca == len(a)-1:
                return True
            ca += 1
            cb -= 1


print(isinverse(11, 11))