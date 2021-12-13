
f = open("numerot.txt", "r")
oldNumber = f.readline()
count = 0
for number in f:
    if int(number) > int(oldNumber):
        count +=1
        print("num" + number + "oldnum" + oldNumber)
    oldNumber = number

