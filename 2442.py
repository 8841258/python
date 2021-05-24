A = int(input())
for i in range(1, A + 1) :
    print(" " * (A - i), end="")
    print("*" * (2 * i - 1))

for i in range(1, A + 1) :
    print(" " * (A - i) + "*" * (2 * i - 1))