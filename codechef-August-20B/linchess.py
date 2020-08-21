try:
    t = int(input())
    while t:
        t -= 1
        win, ans = 999999999999999, 0
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        for num in arr:
            if k % num == 0:
                if k//num < win:
                    win = k//num
                    ans = num

        if ans == 0:
            print(-1)
        else:
            print(ans)
except:
    pass
