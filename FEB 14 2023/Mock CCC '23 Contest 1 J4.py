alpha = [None, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
         "v", "w", "x", "y", "z"]


def recurse(s, v, b, n) :
    if b != 1 :
        for i in range(1, 27) :
            v2 = v + i
            b2 = b - 1
            if v2 > n or (v2 == n and b2 != 0) or (v2 + 26 * b2) < n or (v2 + 1 * b2) > n :
                pass
            else :
                s[len(s) - b] = i
                v += i
                b -= 1
                return recurse(s, v, b, n)
    else :
        s[len(s) - b] = N - v
        return s


N = int(input())
string = input()
stringList = []
value = 0
blanks = 0
for i in range(len(string)) :
    if string[i] in alpha :
        stringList.append(alpha.index(string[i]))
        value += alpha.index(string[i])
    if string[i] == "*" :
        stringList.append(1)
        blanks += 0
if value > N or (value == N and blanks != 0) or (value + 26 * blanks) < N or (value + 1 * blanks) > N :
    print("Impossible")

else :
    final = recurse(stringList, value, blanks, N)
    string = ""
    for i in range(len(final)) :
        string += alpha[final[i]]
    print(string)
