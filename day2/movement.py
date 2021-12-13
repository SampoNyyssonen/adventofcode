verpos = 0
horpos = 0
f = open("day2/2.txt", "r")
for order in f:
    spacepos = order.index(" ")
    cmd = order[0:spacepos]
    value = order[spacepos+1:len(order)]
    if cmd == "up":
        verpos -= int(value)
    elif cmd == "down":
        verpos += int(value)
    elif cmd == "forward":
        horpos += int(value)
    elif cmd == "backward":
        horpos -= int(value)

print("vertical position: "+ str(verpos) + "\n"
        "horizontal position: " +str(horpos) + "\n"
        "multiplied: " + str(verpos * horpos))
    