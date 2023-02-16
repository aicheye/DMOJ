for i in range(10) :
    N, K = [int(i) for i in input().split()]
    packages = [int(i) for i in input().split()]
    packages.sort(reverse=True)
    maxValue = 0
    for j in range(K) :
        maxValue += (packages[j])
    print(maxValue)
    if i != 9 :
        input()
