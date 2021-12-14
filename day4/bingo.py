f = open("day4/4.txt", "r")
bingoNumbers = f.readline()
f.readline()
#Create tables:
bingoTable = []
allTables = []
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
for line in f:
    if len(line) > 3:
        #line to numbers
        bingoRow = findNextNumbers(line," ")
        bingoTable.append(bingoRow)
        #bingoTable.append(line)
    else:
        allTables.append(bingoTable)
        bingoTable = []

#bingopelin ajo
numberArray = findNextNumbers(bingoNumbers, ",")
checkTable = allTables
winTable = []
winNumber = 0
for number in numberArray:
    if (winNumber == 0):
        for i, table in enumerate(allTables):
            for j, row in enumerate(table):
                for k, tableValue in enumerate(row):
                    if tableValue == number:
                        allTables[i][j][k] = 0 #merkataan osuma nollalla 
                                            #(koska tehtävä ei vaadi tiedon säilytystä)
                if allTables[i][j][0] == allTables[i][j][1] == allTables[i][j][2] == allTables[i][j][3] == allTables[i][j][4]:
                    wintable = table
                    winNumber = number
                    print("voittotable: " + str(wintable))
                    #TODO voitto
            table_T = table
            for l in range(len(table)):
                for k in range(len(table[0])):
                    table_T[k][l] = table[l][k]
            for j, row in enumerate(table):
                if table_T[j][0] == table_T[j][1] == table_T[j][2] == table_T[j][3] == table_T[j][4]:
                    #pystyrivivoitto
                    wintable = table
                    winNumber = number
                    print("voittotable2: " + str(wintable))