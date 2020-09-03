test = int(input())
for i in range(test):
    n, country = input().split()
    score = 0
    for i in range(int(n)):
        case = input().split()
        if case[0] == "CONTEST_WON":
            score += 300 + ((20-int(case[1])) if int(case[1]) < 20 else 0)
        elif case[0] == "TOP_CONTRIBUTOR":
            score += 300
        elif case[0] == "BUG_FOUND":
            score += int(case[1])
        elif case[0] == "CONTEST_HOSTED":
            score += 50
    if country == "INDIAN":
        res = score // 200
    else:
        res = score // 400
    print(res)
