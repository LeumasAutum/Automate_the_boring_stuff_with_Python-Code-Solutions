# List to Dictionary Function for Fantasy Game Inventory
# Imagine that a vanquished dragon’s loot is represented as a list of strings 
# like this:
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# Write a function named addToInventory(inventory, addedItems), where the 
# inventory parameter is a dictionary representing the player’s inventory (like 
# in the previous project) and the addedItems parameter is a list like dragonLoot. 
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(inventory, dragonLoot)
print("Inventory:")
for k, v in inventory.items():
    print(v, k)
print("Total number of items:", sum(inventory.values()))
