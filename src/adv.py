from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
# 
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("Damon", room['overlook'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

playing = True

while playing is True:

#printing out current player name and room description
#TODO: set up string method in player class so that it prints player's name, current room, and description
#current room
    print(player1)

#user input: x = input("Enter comma-separated numbers: ").split(',')
    #need a direction for the player to move in n, s, e, w????
    #if there is no room in that direction: error(can't go that way)
    #if there is a room in that direction: restart loop and say player's room and description
    direction = input("Which direction would you like to go? N, E, S, or W?: ")
    # if direction == 'n' and player1.current_room.n_to is not False:
    #     new_room = player1.current_room.n_to
    #     player1.current_room = new_room
    if direction == 'n':
        player1.north()
    if direction == 'e':
        player1.east()
    if direction == 's':
        player1.south()
    if direction == 'w': 
        player1.west()
    if direction == 'q':
        exit()
    
