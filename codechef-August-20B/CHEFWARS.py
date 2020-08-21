import math

try:
    t = int(input())
    while t:
        t -= 1
        h, p = list(map(int, input().split()))

        if h//2 >= p:
            print('0')
        else:
            print('1')
except:
    pass
