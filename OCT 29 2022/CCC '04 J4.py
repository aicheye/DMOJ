alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rDict = dict([(x[1], x[0]) for x in enumerate(alpha)])
keys = input().upper()
toEncode = input().upper()
encoded = ""
currChar = 0
for i in range(len(toEncode)) :
    if toEncode[i] not in alpha :
        pass
    else :
        keyChar = keys[(currChar % len(keys))]
        keyCharPos = rDict[keyChar]
        char = toEncode[i]
        charPos = rDict[char]
        encoded += alpha[(charPos + keyCharPos) % 26]
        currChar += 1

print(encoded)
