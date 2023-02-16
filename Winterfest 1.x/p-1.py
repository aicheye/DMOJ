import math

for i in range(10) :
    W, L, N = [int(i) for i in input().split()]
    print(math.ceil(N / (L * W)))
    if i != 9 :
        input()
