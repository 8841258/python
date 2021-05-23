Chang = 100
Sang = 100
R = int(input())

for i in range(R) :
    ch, sa = map(int, input().split())
    if ch > sa :
        Sang -= ch
    elif ch < sa :
        Chang -= sa

print(Chang)
print(Sang)
