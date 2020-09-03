test = int(input())
while test:
    test -= 1
    count = 1
    n = int(input())
    arr = list(map(int, input().split()))
    new = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < new:
            new = arr[i]
            count += 1

    print(count)
