# Choose your own adventure

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You come to the end of a hallway. Choose to go Left or Right. \n").lower()

if direction =='right':
    print('You stepped on a trap and were impaled by an arrow. \nGame Over!')
else:
    stair = input("You have reached a staircase. Choose to go Up or Down.\n").lower()
    if stair == "down":
        print('The stairs turn into a slide and you slide into hot lava. \nGame Over!')
    else:
        door = input('You reached a room with 3 doors. Red, Blue, Yellow. Choose your destiny!\n').lower()
        if door == 'red':
            print('Red is for fire idiot.\nYou are burned alive.\nGame Over!')
        elif door =='blue':
            print("You step into the open air and fall to your death.\nGame Over!")
        elif door == "yellow":
            print("Yellow the color of gold.\nYou Win!")
        else:
            print("That wasn't even a choice.\nDie of stupidity\nGame Over!")
            