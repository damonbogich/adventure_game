from room import Room
from player import Player
from item import Item

#declare all items
items = {
    'sword': Item('Sword', 'Double edged sword'),
    'basketball': Item('Basketball', "Used to play a game that hasn't been invented yet"),
    'iphone': Item('Iphone', 'Magical communication device from the future'),
    'coffee': Item('Coffee', 'Potion to help one awake in the morning'),
    'cigarettes': Item('Cigarettes', 'Tobacco infused death sticks'),
    'notebook': Item('Notebook', 'Used for writing.  Also a love story.')
}
# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['sword'], items['notebook']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['iphone']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['coffee']]),

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
player1 = Player("Damon", room['outside'], [items['basketball'], items['cigarettes']])
player_item_names = [item.name for item in player1.items]
# for item in player1.items:
#     print(item.name)
# print(room['outside'].items.name)
# print(room['foyer'].items.name)
# print(room['overlook'].items.name)

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
    the_items = player1.current_room.room_items()
    player1.print_items()
    print(f"{player1.current_room.name}'s items:", the_items)
    
    current_room = player1.current_room

    #give player the ability to pickup items from a room:
        #parser that asks the player if he would like to 
    take_room_item_option = input("type in 'take (item name)' to take the item or 'no' to move on: ").split(' ')
    # print(take_room_item_option)
    if len(take_room_item_option) == 0:
        print("you did not type anything")
    elif len(take_room_item_option) == 1:
        first_input_word = take_room_item_option[0]
    elif len(take_room_item_option) == 2:
        first_input_word = take_room_item_option[0]
        second_input_word = take_room_item_option[1]
    else:
        print('you entered too many words')

        #if player types in 'no', then we move on 
    
    if take_room_item_option == 'no':
        print('fine, you get nothing!')
        
    #trying to figure out how to check if the name of an item matches the input:
    elif first_input_word == 'take':
        
        if second_input_word in the_items:
            for item in items.values():
                if item.name == second_input_word:
                    player1.take_item(item)
                    #need the room to drop the item
                    current_room.item_picked_up(item)
        else:
            print("that isn't there")
                
            

    direction = input("Which direction would you like to go? N, E, S, or W?: ")

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
    
