from typing import List, Dict


class Point :
    def __init__(self, x: int, y: int) :
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def __repr__(self) :
        if str(self) is not None :
            return str(self)
        else :
            return "()"

    def __eq__(self, other) :
        if isinstance(other, Point) and other.x == self.x and other.y == self.y :
            return True
        else :
            return False

    def __hash__(self):
        return hash((self.x, self.y))

    def north(self):
        return Point(self.x, self.y + 1)

    def east(self):
        return Point(self.x + 1, self.y)

    def south(self):
        return Point(self.x, self.y - 1)

    def west(self):
        return Point(self.x - 1, self.y)


class Edge :
    def __init__(self, point1, point2) :
        self.start = point1
        self.end = point2
        if self.end.x > self.start.x :
            self.dir = "N"
        if self.end.y > self.start.y :
            self.dir = "W"
        if self.end.x < self.start.x :
            self.dir = "S"
        if self.end.y < self.start.y :
            self.dir = "E"

    def __str__(self) :
        return "[(%s, %s) - (%s, %s)] | %s" % (self.start.x, self.start.y, self.end.x, self.end.y, self.dir)

    def __repr__(self) :
        if str(self) is not None :
            return str(self)
        else :
            return "[]"

    def length(self):
        return int(((self.start.x - self.end.x) ** 2 + (self.start.y - self.end.y) ** 2) ** (1 / 2))

    def next(self) :
        unit = int(((self.start.x - self.end.x) ** 2 + (self.start.y - self.end.y) ** 2) ** (1 / 2)) // 3
        dirUnits = {"N" : [unit, 0],
                    "W" : [0, unit],
                    "S" : [-unit, 0],
                    "E" : [0, -unit]}
        array = {"N" : [dirUnits["N"], dirUnits["W"], dirUnits["N"], dirUnits["E"], dirUnits["N"]],
                 "E" : [dirUnits["E"], dirUnits["N"], dirUnits["E"], dirUnits["S"], dirUnits["E"]],
                 "S" : [dirUnits["S"], dirUnits["E"], dirUnits["S"], dirUnits["W"], dirUnits["S"]],
                 "W" : [dirUnits["W"], dirUnits["S"], dirUnits["W"], dirUnits["N"], dirUnits["W"]]}
        newEdge1 = Edge(self.start,
                        Point(self.start.x + array[self.dir][0][0], self.start.y + array[self.dir][0][1]))
        newEdge2 = Edge(newEdge1.end,
                        Point(newEdge1.end.x + array[self.dir][1][0], newEdge1.end.y + array[self.dir][1][1]))
        newEdge3 = Edge(newEdge2.end,
                        Point(newEdge2.end.x + array[self.dir][2][0], newEdge2.end.y + array[self.dir][2][1]))
        newEdge4 = Edge(newEdge3.end,
                        Point(newEdge3.end.x + array[self.dir][3][0], newEdge3.end.y + array[self.dir][3][1]))
        newEdge5 = Edge(newEdge4.end,
                        Point(newEdge4.end.x + array[self.dir][4][0], newEdge4.end.y + array[self.dir][4][1]))
        return newEdge1, newEdge2, newEdge3, newEdge4, newEdge5


class SquareKochCurve :
    def __init__(self, level, width) :
        self.edges = [Edge(Point(0, 1), Point(width - 1, 1))]
        self.level = level
        self.getStage()
        self.edges.append(Edge(Point(width - 1, 1), Point(0, 1)))

    def __str__(self):
        string = "{"
        for i in range(len(self.edges)) :
            string += str(self.edges[i])
            if i != len(self.edges) - 1 :
                string += "; "
        string += "}"
        return string

    def __repr__(self):
        if str(self) is not None :
            return str(self)
        else :
            return "{}"

    def nextStage(self) :
        stage = []
        for i in range(len(self.edges)) :
            newEdges = Edge(self.edges[i].start, self.edges[i].end).next()
            for j in range(len(newEdges)) :
                stage.append(newEdges[j])
        self.edges = stage

    def getStage(self) :
        for i in range(self.level) :
            self.nextStage()


def fillCurve(d: Dict[Point, List[str]], s: List[Point], w: int, ps: List[List[int]]) :
    if len(s) == 0 :
        return ps
    curr = s[len(s) - 1]
    ps[curr.y][curr.x] = 1
    for i in range(len(d[curr])) :
        if d[curr][i] == "N" :
            p = curr.north()
        elif d[curr][i] == "E" :
            p = curr.east()
        elif d[curr][i] == "S" :
            p = curr.south()
        else :
            p = curr.west()
        if p not in d and 0 <= p.x < w:
            d[p] = ["N", "E", "S", "W"]
            s.append(p)
    if len(s) > 0 :
        s.remove(curr)
        print(s)
        return fillCurve(d, s, w, ps)
      



if __name__ == "__main__" :
    width = 9 + 1
    translations = {"N" : [1, 0],
                    "W" : [0, 1],
                    "S" : [-1, 0],
                    "E" : [0, -1]}
    fractal = SquareKochCurve(1, width)
    pointDirs = {}
    stack = []
    points = []
    for x in range(width) :
        points.append([])
        for y in range(width) :
            points[x].append(0)
    for edge in range(len(fractal.edges)) :
        direction = fractal.edges[edge].dir
        for point in range(fractal.edges[edge].length()) :
            newPoint = Point(fractal.edges[edge].start.x + int(translations[direction][0] * point),
                             fractal.edges[edge].start.y + int(translations[direction][1] * point))
            if newPoint.x <= width :
                if newPoint not in pointDirs :
                    pointDirs[newPoint] = ["N", "E", "S", "W"]  
                    stack.append(newPoint)
                points[newPoint.x][newPoint.y] = 1
            pointDirs[newPoint].remove(direction)
    print(fillCurve(pointDirs, stack, width, points))
