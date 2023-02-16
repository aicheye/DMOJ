text = input()
string = input()
shifts = [string]
hasShift = "no"
for i in range(len(string)) :
    shifted = shifts[len(shifts) - 1][len(string) - 1] + shifts[len(shifts) - 1][:len(string) - 1]
    shifts.append(shifted)
for i in range(len(text) - len(string) + 1) :
    mask = text[i:(i + len(string))]
    for j in range(len(shifts)) :
        if mask == shifts[j] :
            hasShift = "yes"
            break
print(hasShift)
