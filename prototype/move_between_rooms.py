"""Module Six Milestone starter for the simplified movement prototype."""


rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

#set players starting room
current_room = "Great Hall"

#game loop to keep playing and tell the current room
while True:
    print(f"You are in the {current_room}.") 

    #prompts player to enter direction
    command = input("Enter your next move: ")

    #tells player if they chose right direction
    if command in ["north", "south", "east", "west"]:

        if command in rooms[current_room]:

            current_room = rooms[current_room][command]

        #tells player they chose wrong way
        else:
            print("Wrong way")

#tells player they need to try again
    else:
        print("Try again")


