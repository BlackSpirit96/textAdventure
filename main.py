from sys import exit

def died(text, action):
	print_text("%s You died trying to %s. Game Over!" % (text, action))
	exit(0)

def print_text(text):
	print '-' * 70
	print text
	print '-' * 70
	
def room_1(inventory):
	room_title = "Bedroom"
	message = """
	You wake up in a small room with a bed and a book on a desk.
	There is also a door and a window that you can see outside.
	what will you do ?
	"""
	help_message = """
	Welcome to the textAdventure.
	You can perform varius actions like <pick>, <read>, <open>, <where>, <info>.
	But be careful the world is cruel.
	Have fun,
	Black Spirit.
	"""
	print_text(message)
	
	while True:
		
		action = raw_input("> ")
		
		if 'read book' in action:
			print_text(help_message)
		elif 'look' in action or 'watch' in action:
			view = 'It looks like you are in a dence forest with no openings.'
			print_text(view)
		elif 'open' in action and 'door' in action:
			print_text('You "%s" and you procced to the next room' % action)
			room_2(inventory)
		elif 'where' in action:
			print_text("You're in %s!" % room_title)
		elif 'info' in action:
			print_text(message)
		else:
			print_text("%r isn't a valid action!" % action)
		
def room_2(inventory):
	room_title = 'Hallway room'
	message = """
	You entered in the hallway room, so it must be a castle where you are
	because the decoration is medieval like. There are two doors, one green
	and one yellow. There are also stairs that they lead up. Moreover there
	is a big gate, maybe it is the front gate. But what catches your eye fast
	is a red chest with a locket on it.
	"""
	print_text(message)
	
	while True:
		
		action = raw_input("> ")
		
		if 'open' in action and 'door' in action and 'yellow' in action:
			print_text('You "%s" and you procced to the next room' % action)
			room_3(inventory)
		elif 'open' in action and 'chest' in action and 'yellow key' in inventory:
			print_text('There is a green key and a bag of gold! You take both.')
			inventory.append('bag of gold')
			inventory.append('green key')
		elif 'open' in action and 'chest' in action and not( 'yellow key' in inventory):
			died('The chest was traped, and a lamp have fallen on you!', action)
		elif 'open' in action and 'door' in action and 'green' in action:
			if 'green key' in inventory:
				print_text('You "%s" and you procced to the next room' % action)
				room_4(inventory)
			else:
				print_text("This door seems impossible to open without a key!")
		elif 'stairs' in action:
			print_text('You "%s" and you procced to the next room' % action)
			room_7(inventory)
		elif 'main door' in action:
			print_text('That gate is sealed with wooden planks')
		elif 'where' in action:
			print_text("You're in %s!" % room_title)
		elif 'info' in action:
			print_text(message)
		else:
			print_text("%r isn't a valid action!" % action)
		
def room_3(inventory):
	room_title = "Storage Room"
	message = """
	You entered in a room without windows, it will be probable the storage room.
	There are stairs that lead down and the door to get back to the Hallway. There is
	also a big wooden box and a pile of papers on the ground.
	"""
	note_text = """
	You found a secret note.
				*****************************
		There are varius secrets in the game. You should search them, 
	but there are not too hard to figure out.
				*****************************
	"""
	box_text = """
	https://www.youtube.com/watch?v=dQw4w9WgXcQ
	"""
	
	print_text(message)
	
	while True:
		action = raw_input("> ")
		
		if 'open' in action and 'door' in action:
			print_text('You "%s" and you procced to the next room' % action)
			room_2(inventory)
		elif 'stairs':
			print_text('You "%s" and you procced to the next room' % action)
			room_5(inventory)
		elif 'search' in action and 'pile' in action:
			print_text(note_text)
		elif 'box':
			print_text(box_text)
		elif 'where' in action:
			print_text("You're in %s!" % room_title)
		elif 'info' in action:
			print_text(message)
		else:
			print_text("%r isn't a valid action!" % action)

def room_4(inventory):
	room_title = 'Treasure Romm'
	message = """
	Just WoW ! The room is made of gold !!!!
	There is a pile of gold (treasure) the door that leads you back to the
	Hallway and also a small passage.
	"""
	win_text = """
	You take the treasure and you leave peacefully the castle.
	But after you leave the castle dissapears and you didn't learned all
	the secrets about it. Long time latter you regret about it thinking that it
	may have been more treasure. You greedy monster.
	"""
	passage_text = """
	That passage leads to the underground. You fall to the underground
	and you accelerate !!!!!!! Dead end. You die.
	"""
	
	
	print_text(message)
	
	while True:
		action = raw_input('> ')
		
		if 'door' in action:
			print_text('You "%s" and you procced to the next room' % action)
			room_2(inventory)
		elif 'take' in action and 'treasure' in action:
			print_text(win_text)
			exit(0)
		elif 'search' in action and 'treasure' in action and not "Black Key" in inventory:
			print_text("You have found a black key. Where will it lead ?")
			inventory.append("Black Key")
		elif "passage":
			died(passage_text, action)
		elif 'where' in action:
			print_text("You're in %s!" % room_title)
		elif 'info' in action:
			print_text(message)
		else:
			print_text("%r isn't a valid action!" % action)
			
def room_5(inventory):
	pass
	
def room_6(inventory):
	pass
	
def room_7(inventory):
	pass

def main(cheatmone = False):
	inventory = []
	room_1(inventory)

if __name__ == "__main__":
    main()