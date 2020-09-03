test = int(input())
for _ in range(test):
    n = int(input())
    s = input()
    arr = []
    for i in range(n):
        arr.append(s[i:i+n])
        
    ans = ""
    
    for i in range(len(arr)):
        ans += arr[i][i]
        
    print(ans)