f = open("day3/3.txt", "r")
row = []
matrix = []
l = 0
gammaOnes = [0,0,0,0,0,0,0,0,0,0,0,0]
gammaZeros = [0,0,0,0,0,0,0,0,0,0,0,0]
gammaCode = [0,0,0,0,0,0,0,0,0,0,0,0]
epsilonCode = [0,0,0,0,0,0,0,0,0,0,0,0]
oxyMatrix = []


for line in f:
    i = 0
    row = []
    while i < len(line)-1:
        row.append(int(line[i]))
        if int(line[i]) == 1:
            gammaOnes[i] += 1
        else:
            gammaZeros[i] += 1
        i += 1
    matrix.append(row)
    l += 1

i = 0
gammaVal = 0
epsilonVal = 0
while i < len(gammaOnes):
    if gammaOnes[i] >= gammaZeros[i]:
        gammaCode[i] = 1
        epsilonCode[i] = 0
    else:
        gammaCode[i] = 0
        epsilonCode[i] = 1
    i+=1
oxyMatrix = []
newMatrix = matrix
i = 0
for i in range(len(gammaCode)):
    gammaOnes = [0,0,0,0,0,0,0,0,0,0,0,0]
    gammaZeros = [0,0,0,0,0,0,0,0,0,0,0,0]
    oxyMatrix = []
    for k in range(len(newMatrix)):
        if newMatrix[k][i] == 1:
            gammaOnes[i] += 1
        else:
            gammaZeros[i] += 1
    
    #for l in range(len(gammaOnes)):
    if gammaOnes[i] >= gammaZeros[i]:
        gammaCode[i] = 1
        epsilonCode[i] = 0
    else:
        gammaCode[i] = 0
        epsilonCode[i] = 1

    for j in range(len(newMatrix)):
        if int(newMatrix[j][i]) == gammaCode[i]:
            oxyMatrix.append(newMatrix[j])
    newMatrix = oxyMatrix
#scrubber rating
co2Matrix = []
newMatrix = matrix
i = 0
k = 0
j = 0
l = 0
for i in range(len(gammaCode)):
    gammaOnes = [0,0,0,0,0,0,0,0,0,0,0,0]
    gammaZeros = [0,0,0,0,0,0,0,0,0,0,0,0]
    co2Matrix = []
    for k in range(len(newMatrix)):
        if newMatrix[k][i] == 0:
            gammaZeros[i] += 1
        else:
            gammaOnes[i] += 1
    
#for l in range(len(gammaOnes)):
    if gammaOnes[i] >= gammaZeros[i]:
        gammaCode[i] = 1
        epsilonCode[i] = 0
    else:
        gammaCode[i] = 0
        epsilonCode[i] = 1

    for j in range(len(newMatrix)):
        if int(newMatrix[j][i]) == epsilonCode[i]:
            co2Matrix.append(newMatrix[j])
    newMatrix = co2Matrix
    if len(newMatrix) == 1:
        break

oxyVal, co2Val, i = 0,0,0
#convert to 
for i in range(12):
    if oxyMatrix[0][i] == 1:
        oxyVal += pow(2,len(oxyMatrix[0])-i-1)
    if co2Matrix[0][i] == 1:
        co2Val += pow(2,len(co2Matrix[0])-i-1)

print("oxyRating: ") 
print(oxyMatrix)
print("co2Rating: ") 
print(co2Matrix)

print("oxyVal: ") 
print(oxyVal)
print("co2Val: ") 
print(co2Val)

print("mul: " + str(oxyVal*co2Val))
