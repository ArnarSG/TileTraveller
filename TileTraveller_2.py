location = "1,1"
while location != "3,1":
    if location == "1,1":
        print("You can travel: (N)orth.")
        dir = input("Direction: ")
        if (dir == "N") or (dir == "n"):
            location = "1,2"
        else:
            print("Not a valid direction!")

    if location == "1,2":
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        dir = input("Direction: ")
        if (dir == "N") or (dir == "n"):
            location = "1,3"
        elif (dir == "E") or (dir == "e"):
            location = "2,2"
        elif (dir == "S") or (dir == "s"):
            location = "1,1"
        else:
            print("Not a valid direction!")

    if location == "1,3":
        print("You can travel: (E)ast or (S)outh.")
        dir = input("Direction: ")
        if (dir == "E") or (dir == "e"):
            location = "2,3"
        elif (dir == "S") or (dir == "s"):
            location = "1,2"
        else:
            print("Not a valid direction!")

    if location == "2,1":
        print("You can travel: (N)orth.")
        dir = input("Direction: ")
        if (dir == "N") or (dir == "n"):
            location = "2,2"
        else:
            print("Not a valid direction!")

    if location == "2,2":
        print("You can travel: (S)outh or (W)est.")
        dir = input("Direction: ")
        if (dir == "W") or (dir == "w"):
            location = "1,2"
        elif (dir == "S") or (dir == "s"):
            location = "2,1"
        else:
            print("Not a valid direction!")

    if location == "2,3":
        print("You can travel: (E)ast or (W)est.")
        dir = input("Direction: ")
        if (dir == "E") or (dir == "e"):
            location = "3,3"
        elif (dir == "W") or (dir == "w"):
            location = "1,3"
        else:
            print("Not a valid direction!")

    if location == "3,3":
        print("You can travel: (S)outh or (W)est.")
        dir = input("Direction: ")
        if (dir == "S") or (dir == "s"):
            location = "3,2"
        elif (dir == "W") or (dir == "w"):
            location = "2,3"
        else:
            print("Not a valid direction!")

    if location == "3,2":
        print("You can travel: (N)orth or (S)outh.")
        dir = input("Direction: ")
        if (dir == "N") or (dir == "n"):
            location = "3,3"
        elif (dir == "S") or (dir == "s"):
            location = "3,1"
        else:
            print("Not a valid direction!")

print("Victory!")
