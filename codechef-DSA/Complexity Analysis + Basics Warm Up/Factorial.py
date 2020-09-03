test = int(input())
while test:
    test -= 1
    count = 0
    n = int(input())
    i = 5
    while n/i >= 1:
        count += n//i
        i *= 5

    print(count)
