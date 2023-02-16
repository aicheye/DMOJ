N, K, M = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
bundling = True
bundles = []
for i in range(N - K) :
    for j in range(i + K, N) :
        if a[i] + b[j] == M :
            bundles.append([i, j])
        if i - j >= 0 :
            if a[i] + b[i - j] == M :
                bundles.append([i, i - j])
print(len(bundles))
