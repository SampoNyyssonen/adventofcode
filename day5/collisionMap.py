f = open("day5/5__.txt", "r")
from enum import Enum
class Dir(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
    DIAGONAL = 3
    OTHER = 4
errCount = 0
class Line:
    x1: int
    y1: int
    x2: int
    y2: int
    def __init__(self, x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def checkLine(self):
        if (self.y1 == self.y2):
            return Dir.HORIZONTAL
        elif (self.x1 == self.x2):
            return Dir.VERTICAL
        elif abs(self.x1-self.x2) == abs(self.y1-self.y2): 
            return Dir.DIAGONAL
        else:
            return Dir.DIAGONAL
class Map:
    XYMap = [[]]
    collCount : int = 0
    errCount : int = 0
    def __init__(self, collCount = 0):
        self.XYMap = [ [ 0 for i in range(1000) ] for j in range(1000) ]
        self.collCount = collCount
    def drawLine(self, line : Line):
        if line.checkLine() == Dir.HORIZONTAL:
            i = line.x1
            if line.x1 <= line.x2:
                stepX = 1
            else: 
                stepX = -1
            while max(line.x2, line.x1) >= i >= min(line.x2, line.x1):
                self.XYMap[line.y1][i] += 1 
                if self.XYMap[line.y1][i] == 2:
                    self.collCount += 1
                i +=stepX
            return
        elif line.checkLine() == Dir.VERTICAL:
            i = line.y1
            if line.y1 <= line.y2:
                stepY = 1
            else: 
                stepY = -1
            while max(line.y2, line.y1) >= i >=  min(line.y2, line.y1):
                self.XYMap[i][line.x1] += 1
                if self.XYMap[i][line.x1] == 2:
                    self.collCount += 1
                i +=stepY
            return
        elif line.checkLine() == Dir.DIAGONAL:
            i = line.y1
            j = line.x1
            stepY = 1
            stepX = 1
            if line.y1 <= line.y2:
                stepY = 1
            else: 
                stepY = -1
            if line.x1 <= line.x2:
                stepX = 1
            else: 
                stepX = -1
            while max(line.y2, line.y1) >= i >= min(line.y2, line.y1):
                self.XYMap[i][j] += 1 
                if self.XYMap[i][j] == 2:
                    self.collCount += 1
                j += stepX 
                i += stepY
            return
        else:
            self.errCount +=1
            return
    def findCollisions(self):
        collisionCount = 0
        for i ,row in enumerate(self.XYMap):
            for j, cell in enumerate(self.XYMap[i]):
                if self.XYMap[i][j] >= 2:
                    collisionCount += 1
        return collisionCount
def findNumPairs(line):
    spacepos1 = line.find(",")
    x1 = int(line[0:spacepos1])
    spacepos2 = line.find(" ")
    y1 = int(line[spacepos1+1:spacepos2])
    valuePair2 = line[spacepos2+1:len(line)]
    spacepos3 = valuePair2.find(" ")
    spacepos4 = valuePair2.find(",")
    spacepos5 = valuePair2.find("\n")
    x2 = int(valuePair2[spacepos3+1:spacepos4])
    y2 = int(valuePair2[spacepos4+1:spacepos5])
    newLine = Line(x1,y1,x2,y2)
    return newLine
myMap = Map()
newLine : Line
for row in f:
    newLine = findNumPairs(row)
    myMap.drawLine(line = newLine)
print(myMap.errCount)
print(myMap.collCount)
print(myMap.findCollisions())