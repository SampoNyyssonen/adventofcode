
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

dayCount = 0
fishNumArray = [0,0,0,0,0,0,0,0,0,0]
fishArr = []

i = 0

#Selvitä montako kalaa syntyy numerosta 8,7,6,5,4,3,2,1 100 päivässä
#Käy taulukko läpi 155 päivän kohdalla 
#ja kerro taulukon jokainen lukema sen numeron 100 päivän lukemalla  

#Selvitä 64 päivän lukemat kullekkin mahdolliselle kalalle
while i < 9:
    fishArr = [i]
    dayCount = 0
    while dayCount < 64:
        unbornBabyCount = 0
        for j, fish in enumerate(fishArr):
            fishArr[j] -= 1
            if fishArr[j] < 0:
                unbornBabyCount +=1
                fishArr[j] = 6
   
        fishArr+=[ 8 for i in range(unbornBabyCount) ]

        dayCount += 1
    fishNumArray[i] = fishArr
    i+=1
    print(len(fishArr))
fish100Array = [0,0,0,0,0,0,0,0,0,0]
i = 0
#selvitä lukema 128 päivälle
while i < 9:
    fishArr = [i]
    dayCount = 0
    while dayCount < 2:
        unbornBabyCount = 0
        newFishArr = []
        oldFishArr = []
        for j, fish in enumerate(fishArr):
            newFishArr += fishNumArray[fishArr[j]]
        fishArr = newFishArr
        newFishArr = []
        #unbornBabyCount -= 1
        dayCount += 1
    fish100Array[i] = len(fishArr)
    i+=1
    print(len(fishArr))
fishArr = [0]
dayCount = 0
fishArr = findNextNumbers(f.readline(), ",")
fishArrBak = fishArr
while dayCount < 64:
    unbornBabyCount = 0
    
    for j, fish in enumerate(fishArr):
        fishArr[j] -= 1
        if fishArr[j] < 0:
            unbornBabyCount +=1
            fishArr[j] = 6
    #while unbornBabyCount >= 1:
    fishArr+=[ 8 for i in range(unbornBabyCount) ]
    #    unbornBabyCount -= 1
    dayCount += 1
print("testi")
print(len(fishArr))


allFishArrays = []
i = 0
#fishArr = findNextNumbers(f.readline(), ",")
dayCount = 0
newFishArr = []
oldFishArr = []
#mennään 128 päivää aloituspoolille
fishArr = fishArrBak
while dayCount < 1:
    unbornBabyCount = 0
    newFishArr = []
    oldFishArr = []
    for i, fish in enumerate(fishArr):
        newFishArr += fishNumArray[fishArr[i]]
    fishArr = newFishArr
    newFishArr = []
    #unbornBabyCount -= 1
    dayCount += 1
    allFishArrays+=fishArr
print(len(allFishArrays))

""" while dayCount < 250:
    unbornBabyCount = 0
    for j, fish in enumerate(fishArr):
        fishArr[j] -= 1
        if fishArr[j] < 0:
            unbornBabyCount +=1
            fishArr[j] = 6
    #while unbornBabyCount >= 1:
    fishArr+=[ 8 for i in range(unbornBabyCount) ]
    #    unbornBabyCount -= 1
    dayCount += 1
    allFishArrays+=fishArr """

#fishArr = findNextNumbers(f.readline(), ",")
#summataan 128 päivää lisää jokaiselle poolin kalalle
fishSum = 0
for i, fish in enumerate(allFishArrays):
    fishSum += fish100Array[allFishArrays[i]]
print(fishSum)