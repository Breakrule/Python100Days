class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add(self, item: Item):
        self.items.append(item)
    
    def total(self) -> int:
        return sum(item.price for item in self.items)
    
    def __len__(self) -> int:
        return len(self.items)

# read input and create Item objects
n = int(input())
items = []
for _ in range(n):
    name, price = input().split()
    items.append(Item(name, int(price)))

# create ShoppingCart object
cart = ShoppingCart()

# perform operations on the ShoppingCart
q = int(input())
for _ in range(q):
    operation = input().split()
    if operation[0] == "add":
        item_name = operation[1]
        item = next((item for item in items if item.name == item_name), None)
        if item is not None:
            cart.add(item)
    elif operation[0] == "total":
        print(cart.total())
    elif operation[0] == "len":
        print(len(cart))
