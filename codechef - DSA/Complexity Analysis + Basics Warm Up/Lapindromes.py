def sol(st):
    dp = [0]*26
    for i in st:
        dp[ord(i)-97] += 1

    return dp


test = int(input())
while test:
    test -= 1
    s = input()
    n = len(s)
    r = n//2
    if n % 2 == 0:
        s1 = sol(s[:r])
        s2 = sol(s[r:])
    else:
        s1 = sol(s[:r])
        s2 = sol(s[r+1:])
        #print(s[:r], s[r+1:])
    if s1 == s2:
        print("YES")
    else:
        print("NO")
