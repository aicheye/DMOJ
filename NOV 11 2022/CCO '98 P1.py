def fib(n) :
    if arr[n] != -1 :
        return arr[n]
    else :
        arr[n] = fib(n-1) + fib(n-2)
        return arr[n]


ns = []
greatestN = 1
while True :
    nIn = int(input())
    if nIn <= 0 :
        break
    else:
        if nIn > greatestN :
            greatestN = nIn
        ns.append(nIn)
arr = [-1] * (greatestN + 1)
if len(arr) > 1 :
    arr[0] = 0
    arr[1] = 1
    if len(arr) > 2 :
        arr[2] = 1
for i in range(len(ns)) :
    print(fib(ns[i]))
