f = open("day6/6.txt", "r")
def findNextNumbers(line, separator):
    spacepos = line.find(separator)
    if spacepos == -1:
        spacepos = line.find("\n")
        number = int(line[0:spacepos])
        returnRow = [number]
        return returnRow
    elif spacepos == 0:
        return findNextNumbers(line[spacepos+1:len(line)], separator)
    if len(line[0:spacepos]) != 0:
        number = int(line[0:spacepos])
        returnRow = [number]
        returnRow += findNextNumbers(line[spacepos+1:len(line)], separator)
        return returnRow
    else:
        return
def fishCheck(fish):
    fish -= 1
    if fish < 0:
        return 6
    else:
        return fish
fishArr = findNextNumbers(f.readline(), ",")
dayCount = 0
print(len(fishArr))
while dayCount < 50:
    unbornBabyCount = 0
    i = 0
    for i, fish in enumerate(fishArr):
        fishArr[i] = fishCheck(fishArr[i])
        if fishArr[i] == 6:
            unbornBabyCount +=1
    #while unbornBabyCount >= 1:
    fishArr+=[ 8 for i in range(unbornBabyCount) ]
    #    unbornBabyCount -= 1
    dayCount += 1
print(len(fishArr))