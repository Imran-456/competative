test = int(input())
for i in range(test):
    k, d1, d2 = list(map(int, input().split()))
    ans = d1+d2
    if k == 2:
        if ans % 3 == 0:
            print("YES")
        else:
            print("NO")
        continue
    ans += (d1+d2) % 10
    k -= 3
    ans += (2 * (d1+d2) % 10) * (k // 4)
    ans += (4 * (d1+d2) % 10) * (k // 4)
    ans += (8 * (d1+d2) % 10) * (k // 4)
    ans += (6 * (d1+d2) % 10) * (k // 4)
    k %= 4
    if(k > 0):
        ans += 2 * (d1+d2) % 10
        k -= 1
    if(k > 0):
        ans += 4 * (d1+d2) % 10
        k -= 1
    if(k > 0):
        ans += 8 * (d1+d2) % 10
        k -= 1
    if(k > 0):
        ans += 6 * (d1+d2) % 10
        k -= 1
    if(ans % 3 == 0):
        print("YES")
    else:
        print("NO")
