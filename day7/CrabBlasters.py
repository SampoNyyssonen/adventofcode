
f = open("day7/7.txt", "r")
def findNextNumbers(line, separator):
    spacepos = line.find(separator)
    if spacepos == -1:
        spacepos = line.find("\n")
        if spacepos == -1:
            spacepos = len(line)
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
crabPositions = findNextNumbers(f.readline(),",")