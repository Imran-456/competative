test = int(input())
while test:
    k = input()[::-1]
    i = 0
    while k[i] == '0':
        i += 1
    print(k[i:])
