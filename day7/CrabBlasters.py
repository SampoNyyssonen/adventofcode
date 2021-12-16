
f = open("day7/7.txt", "r")
def distCalc(val):
    sum = 0
    while val > 0:
        sum += val
        val -= 1
    return sum
def findNextNumbers(line, separator):
    spacepos = line.find(separator)
    returnRow = []
    while spacepos != -1:
        if len(line[0:spacepos]) != 0:
            number = int(line[0:spacepos])
            returnRow.append(number)
            line = line[spacepos+1:len(line)]
            spacepos = line.find(separator)
    if spacepos == -1:
        spacepos = line.find("\n")
        if spacepos == -1:
            spacepos = len(line)
        number = int(line[0:spacepos])
        returnRow.append(number)
        return returnRow
crabPositions = findNextNumbers(f.readline(),",")

#print(crabPositions)
sumFuel = [0 for i in range(200)]
avg = round(sum(crabPositions) / len(crabPositions))
tryArea = list(range(avg - 000, avg + 200))
for j, point in enumerate(tryArea):
    for i, crabs in enumerate(crabPositions):
        sumFuel[j] += distCalc(abs(crabPositions[i]-tryArea[j]))

print(min(sumFuel))