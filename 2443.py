A = int(input())

for i in range(A, 0, -1) :
    print(" " * (A-i) + "*" * (2*i-1))
