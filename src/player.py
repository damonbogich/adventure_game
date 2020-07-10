# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.items = items
    def __str__(self):
        return f"You are in {self.current_room.name}.  {self.current_room.description}"
    
    def print_items(self):
        item_list = [item.name for item in self.items]
        # print('your items currently include:', item_list)
        return item_list

    def take_item(self,item):
        print(f"you took the {item.name}!")
        self.items.append(item)
    
    def north(self):
        try:
            if self.current_room.n_to is not None:
                new_room = self.current_room.n_to
                self.current_room = new_room
        except AttributeError:
            print("Can't move that way from here")

    def east(self):
        try:
            if self.current_room.e_to is not None:
                new_room = self.current_room.e_to
                self.current_room = new_room
        except AttributeError:
            print("Can't move that way from here")
    
    def south(self):
        try:
            if self.current_room.s_to is not None:
                new_room = self.current_room.s_to
                self.current_room = new_room
        except AttributeError:
            print("Can't move that way from here")
    
    def west(self):
        try:
            if self.current_room.w_to is not None:
                new_room = self.current_room.w_to
                self.current_room = new_room
        except AttributeError:
            print("Can't move that way from here")

    

    
    
    # def west(self):
    #     if self.current_room.w_to != None:
    #         new_room = self.current_room.w_to
    #         self.current_room = new_room
    #     else:
    #         print("Can't move that way from here")
    #         return None