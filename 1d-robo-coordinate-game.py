# STEP 3
# x ----R----- >
# CONTROLS : "a" - left, "d" - right

LENGTH = 10
roboX  = 5

# game loop
while True:
 ########## DRAW THE MAP #########
    print("\n") # + "\n"
    x = 1
    while x <= LENGTH:
        if x == roboX:
            print("R", end="") # "\n"
        else:
            print("-", end="") # "\n"
        x += 1 
    print("\n") # + "\n"  
 ## ####### DRAW THE MAP ##########

 ### ###### CONTROLS ##########
    direction = input("dir(a/d) >>>")
    if direction == "a":
        roboX -= 1
    if direction == "d":
        roboX += 1
 ########## CONTROLS ##########

