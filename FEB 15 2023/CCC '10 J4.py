while True :
    temps = [int(i) for i in input().split()]
    if len(temps) == 1 and temps[0] == 0 :
        break
    else :
        deltas = []
        for i in range(len(temps) - 1) :
            deltas.append(temps[i+1] - temps[i])
        cycle = []
