
f = open("day1/numerot.txt", "r")
olderNumber = int(f.readline())
oldNumber = int(f.readline())
number = int(f.readline())
oldSum = olderNumber + oldNumber + number
count = 0
for number in f:
    sum = olderNumber + oldNumber + int(number)
    if sum > oldSum:
        count +=1
        ##print("num" + number + "oldnum" + oldNumber)
    oldSum = sum
    olderNumber = oldNumber
    oldNumber = int(number)
    
print(count)
