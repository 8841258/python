# 위쪽 세모
A = int(input())
for i in range(1, A + 1) :
    print(" " * (A - i) + "*" * (2 * i - 1))

# 아래쪽 세모
for i in range(A, 1, -1) :
    print(" " * (A-i + 1) + "*" * (2*(i-1)-1))

