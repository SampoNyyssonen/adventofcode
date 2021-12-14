f = open("day3/3.txt", "r")
row = []
matrix = []
l = 0
gammaOnes = [0,0,0,0,0,0,0,0,0,0,0,0]
gammaZeros = [0,0,0,0,0,0,0,0,0,0,0,0]
gammaCode = [0,0,0,0,0,0,0,0,0,0,0,0]
epsilonCode = [0,0,0,0,0,0,0,0,0,0,0,0]
for line in f:
    i = 0
    row = []
    while i < len(line)-1:
        row.append(line[i])
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
        gammaVal += pow(2,len(gammaOnes)-i-1)
        epsilonCode[i] = 0
    else:
        gammaCode[i] = 0
        epsilonCode[i] = 1
        epsilonVal += pow(2,len(gammaOnes)-i-1)
    i+=1

print("gammaOnes: ") 
print(gammaCode)
print("\nEpsiloncode: ") 
print(epsilonCode)
print("\ngammaZeros: ") 
print(gammaZeros)

print("\n GammaVal")
print(gammaVal)
print("\n EpsilonVal")
print(epsilonVal)

print("\n mul")
print(epsilonVal*gammaVal)