# test = int(input())
# for _ in range(test):
#     main = input()
#     sub = input()
#     sol = [0 for i in range(26)]
#     for i in main:
#         sol[ord(i)-97] += 1

#     for i in range(1, len(sub)):
#         sol[ord(sub[i])-97] -= 1
#     st = ""
#     for i in range(len(sol)):
#         if sol[i] != 0:
#             st += (chr(i+97)*sol[i])

#     s = "".join(sorted(st))
#     ele = sub[0]
#     pos = s.rindex(ele)
#     print(s[:pos]+sub[:]+s[pos+1:])

x = "abcdefghijklmnopqrstuvwxyz"
k = [0] * 26
for i in x:
    k[ord(i)-97] += 1

print(*k)
for i in range(len(k)):
    print(chr(i+97), end=" ")
