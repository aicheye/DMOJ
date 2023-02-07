def gcf(a, b):
    x = 1
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if a % i == 0 and b % i == 0:
            x = i
    return x


if __name__ == "__main__":
    N = int(input())
    D = int(input())
    gcfND = gcf(N, D)
    simpleN = N // gcfND
    simpleD = D // gcfND
    if N == 0:
        print("0")
    elif simpleD == 1:
        print(simpleN)
    elif simpleN > simpleD:
        print(str(simpleN // simpleD) + " " + str(simpleN % simpleD) + "/" + str(simpleD))
    else:
        print(str(simpleN) + "/" + str(simpleD))
