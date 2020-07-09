# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = None):
        self.name = name
        self.description = description
        self.items = items
        #pointers
        # self.n_to = n_to
        # self.e_to = e_to
        # self.s_to = s_to
        # self.w_to = w_to
    def room_items(self):
        item_names = [item.name for item in self.items]
        # print(f"{self.name}'s items: {item_names}")
        return item_names
    def item_picked_up(self,item):
        self.items.remove(item)

