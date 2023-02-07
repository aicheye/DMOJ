def isMonkeyWord(string, recursions) :
    recursions += 1
    if recursions > 100 :
        return "NO"
    elif len(string) == 1 and string[0] is True :
        return "YES"
    else :
        for i in range(len(string)) :
            if len(string) == 1 and string[0] is True :
                return "YES"
            elif i == len(string) - 1 :
                return isMonkeyWord(string, recursions)
            elif len(string) < 3 :
                return "NO"
            elif string[i] == "B" and string[i + 1] is True and string[i + 2] == "S" :
                string.pop(i)
                string.pop(i + 1)
                return isMonkeyWord(string, recursions)
            elif string[i] is True and string[i + 1] == "N" and string[i + 2] is True :
                string.pop(i + 1)
                string.pop(i + 1)
                return isMonkeyWord(string, recursions)
        return isMonkeyWord(string, recursions)


inputting = True
while inputting:
    text = input()
    if text == "X" :
        inputting = False
    elif text.count("B") + text.count("A") + text.count("N") + text.count("S") != len(text) :
        print("NO")
    else :
        text = [*text]
        for i in range(len(text)) :
            if text[i] == "A" :
                text[i] = True
        print(isMonkeyWord(text, 0))
