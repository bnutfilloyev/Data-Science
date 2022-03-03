first = ord('A')
last = ord('Z')

for i in range(first, last + 1):
    for j in range(last, first - 1, -1):
        if j <= i:
            print(chr(i), end=' ')
        else:
            print('', end=' ')
    print()



