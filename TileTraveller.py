def moves(x_positon: int, y_positon: int, direction: str):
    ''' Shows how you move in the game'''

    if direction.lower() == 'n':
        return x_positon, y_positon + 1
    elif direction.lower() == 's':
        return x_positon, y_positon - 1
    elif direction.lower() == 'e':
        return x_positon + 1, y_positon
    elif direction.lower() == 'w':
        return x_positon - 1, y_positon
        # það þarf svo bara að setja þetta saman við while lykkjuna fyrir ofan


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
        if (dir == "E") or (dir == "e"):
            location = "2,2"
        if (dir == "S") or (dir == "s"):
            location = "1,2"
        else:
            print("Not a valid direction!")

def moves(x_positon: int, y_positon: int, direction: str):
    ''' Shows how you move in the game'''

    if direction.lower() == 'n':
        return x_positon, y_positon + 1
    elif direction.lower() == 's':
        return x_positon, y_positon - 1
    elif direction.lower() == 'e':
        return x_positon + 1, y_positon
    elif direction.lower() == 'w':
        return x_positon - 1, y_positon
        # það þarf svo bara að setja þetta saman við while lykkjuna fyrir ofan