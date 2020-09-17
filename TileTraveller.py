<<<<<<< HEAD
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

=======
TILE = [1,1]

MAX=3
MIN=1
T=1
W=" "
S= " "
N= " "
E= " " 
NORTH="(N)orth"
WEST="(W)est"
SOUTH="(S)outh"
EAST="(E)ast"
X=1
>>>>>>> 5c58941f440d7e4523fa3ff8381b99e4815f2469
