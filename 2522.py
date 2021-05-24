A = int(input())
[2, 1, 0]
for i in range(A-1, -1, -1) :
    print(" " * i + "*" * (A-i))
    
for i in range(A-1, 0, -1) :
    print(" " * (A-i) + "*" * i)