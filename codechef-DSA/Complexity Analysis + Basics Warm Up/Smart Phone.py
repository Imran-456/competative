n = int(input())
k = []
for i in range(n):
    k.append(int(input()))

k.sort()
ans, cnt = 0, 0
for i in range(n):
    cnt = k[i] * (n-i)
    ans = max(ans, cnt)

print(ans)
