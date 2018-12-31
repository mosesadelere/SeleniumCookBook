
def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i] = inventory[i] + 1
    return inventory

def displayInventory(inventory):
    print('Inventory')
    itemTotal = 0
    for k,v in inventory.items():
        print(v, ' ' + k.rjust(5))
        itemTotal = itemTotal + v
    print('Total number of items: ' + str(itemTotal))

inv = {'gold coin' : 42, 'rope' : 1, 'dagger' : 1, 'arrow' : 12, 'torch' : 6}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'diamond']
inven = addToInventory(inv,dragonLoot)
print(inv)
displayInventory(inven)