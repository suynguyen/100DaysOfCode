left_or_right = input("Welcome to Treasure Island. Your Mission is to find the treasure. left or right?\n4").lower()
if left_or_right == "left":
    swim_or_wait = input("Would you like to swim or wait?\n").lower()
    if swim_or_wait == "wait":
        door_color = input("Which door do you want to open? red, blue, yellow oder anything\n").lower()
        if door_color == "red":
            print("Burned by fire. game over")
        elif door_color == "blue":
            print("Eaten by beasts. Game over")
        elif door_color == "yellow":
            print("You win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over")
else:
    print("Fall into a hole. Game over")


