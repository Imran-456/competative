
import math

test = int(input())

while test:
    test -= 1
    pc, pr = list(map(int, input().split()))
    ans1 = math.ceil(pc/9)
    ans2 = math.ceil(pr/9)

    if ans1 < ans2:
        print("0", ans1)
    else:
        print("1", ans2)
