def displayinventory(inventory):
	count=0
	
	for i in inventory:
		count+=inventory[i]
		print("{0} {1}".format(inventory[i],i))

	print("Total number of items : {}".format(count))

def addtoinventory(inventory , addeditems):

	for i in addeditems:
		inventory.setdefault(i,0)
		inventory[i] += 1


inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayinventory(inventory)
print(" ")
addtoinventory(inventory, dragonLoot)
displayinventory(inventory)