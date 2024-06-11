"""The flowchart represents a decision-based game called "Treasure Island," where the objective is to find the treasure. Here is a detailed description of the decision-making process in the game:

1. **Start**: The game begins with the message "Welcome to Treasure Island. Your mission is to find the treasure."

2. **First Decision - Left or Right?**: The player must choose between going left or right.
   - **Right or anything else**: If the player chooses right or any other direction except left, they fall into a hole and the game is over ("Fall into a hole. Game Over.").
   - **Left**: If the player chooses left, they proceed to the next decision point.

3. **Second Decision - Swim or Wait?**: After choosing left, the player must decide whether to swim or wait.
   - **Swim or anything else**: If the player chooses to swim or anything other than wait, they are attacked by trout and the game is over ("Attacked by trout. Game Over.").
   - **Wait**: If the player chooses to wait, they move on to the next decision point.

4. **Third Decision - Which Door?**: After waiting, the player must choose between three doors: red, blue, or yellow.
   - **Red**: If the player chooses the red door, they are burned by fire and the game is over ("Burned by fire. Game Over.").
   - **Blue**: If the player chooses the blue door, they are eaten by beasts and the game is over ("Eaten by beasts. Game Over.").
   - **Yellow**: If the player chooses the yellow door, they find the treasure and win the game ("You Win!").
   - **Anything else**: If the player chooses any other door, the game is over without specifying a reason ("Game Over.").

The flowchart visually maps out these choices and their consequences, guiding the player through the game based on their decisions."""
#Solution
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("!warning! enter your input in lowwer case")
x = input('You are at a cross road. Where you want to go? Type "left" or "right"\n')
if x == "left":
   y = input('You come to lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n')
   if y == "wait":
       z = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')
       if z == "red":
           print("Burned by fire. Game Over!")
       elif z == "blue":
           print("Eaten by beasts. Game Over!")
       elif z == "yellow":
           print("You Win!")
       else:
           print("Game Over.")    
   else:
       print("Attacked by trout. Game Over.")    
else:
    print("Fall into a hole Game Over.")