if __name__ == '__main__' :
    cr = input().split()
    c = int(cr[0])
    r = int(cr[1])
    currX = 0
    currY = 0
    running = True
    while running:
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
        if xy == ["0", "0"]:
            running = False
            break
        else:
            currX += x
            currY += y
            if currX > c:
                currX = c
            elif currX < 0:
                currX = 0
            if currY > r:
                currY = r
            elif currY < 0:
                currY = 0
            print(str(currX) + " " + str(currY))
