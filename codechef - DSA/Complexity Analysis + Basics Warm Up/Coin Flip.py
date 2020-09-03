test = int(input())
for i in range(test):
    qu = int(input())
    for i in range(qu):
        i, n, q = list(map(int, input().split()))
        if n % 2 == 0:
            ans = n//2
        else:
            if (i == 1 and q == 1) or (i == 2 and q == 2):
                ans = n//2
            elif (i == 1 and q == 2) or (i == 2 and q == 1):
                ans = (n//2) + 1
        print(ans)
