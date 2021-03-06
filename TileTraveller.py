x_positon, y_positon = 1,1
acceptable_moves = ('')
direction = ''

def moves(x_positon: int, y_positon: int, direction: str):
    ''' Shows how you move in the game'''

    if direction.lower() == 's':
        return x_positon, y_positon - 1
    elif direction.lower() == 'n':
        return x_positon, y_positon + 1
    elif direction.lower() == 'w' :
        return x_positon - 1, y_positon
    elif direction.lower() == 'e':
        return x_positon + 1, y_positon

while True: 
    if direction.lower() in acceptable_moves:
        if ((x_positon == 1) and (y_positon == 1)) or ((x_positon == 2) and (y_positon == 1)):
            print("You can travel: (N)orth.")
            acceptable_moves = ('n')   
        elif (x_positon == 1) and (y_positon == 2):
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            acceptable_moves = ('n', 'e', 's') 
        elif (x_positon == 1) and (y_positon == 3):
            print(f"You can travel: (E)ast or (S)outh.")
            acceptable_moves = ('e', 's') 
        elif ((x_positon == 2) and (y_positon == 2)) or ((x_positon == 3) and (y_positon == 3)):
            print(f"You can travel: (S)outh or (W)est.")
            acceptable_moves = ('s', 'w') 
        elif (x_positon == 2) and (y_positon == 3):
            print(f"You can travel: (E)ast or (W)est.")
            acceptable_moves = ('e', 'w') 
        elif (x_positon == 3) and (y_positon == 2):
            print(f"You can travel: (N)orth or (S)outh.")
            acceptable_moves = ('n', 's') 
        elif x_positon == 3 and y_positon == 1:
            print ('Victory!')
            exit()
      
    direction = str(input("Direction: ")) 
    if direction.lower() in acceptable_moves:
        x_positon, y_positon = moves(x_positon, y_positon, direction) 
    else:
        print ('Not a valid direction')
# Nánast komið eitthvað vesen á þessu inn á mími

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