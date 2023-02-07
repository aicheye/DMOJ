alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rDict = dict([(x[1], x[0]) for x in enumerate(alpha)])
K = int(input())
encoded = input()
decoded = ""
for i in range(len(encoded)):
    decoded += alpha[(((rDict[encoded[i]] + 1) - (3 * (i + 1) + K)) % 26) - 1]
print(decoded)
