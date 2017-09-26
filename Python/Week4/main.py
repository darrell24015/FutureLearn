from room import Room
from character import Character,Enemy,Friend

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate decorations.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor.")

# Add an enemy and it's weakness to defeat it
dave = Enemy("Dave","A bad, very smelly Zombie")
dave.set_weakness("cheese")
# Add some conversation for Dave when talked to
dave.set_conversation("Argh, me eat your brains!")

# Add a friend and it's feelings
kati = Friend("Kati","A friendly skeleton")
kati.set_feelings("I'm very happy today!")
# Add some conversation for Kati when talked to
kati.set_conversation("Do you need a hug today?")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Add characters to rooms
dining_hall.set_character(dave)
ballroom.set_character(kati)

# Testing the get_details() method
# dining_hall.get_details()
# kitchen.get_details()
# ballroom.get_details()

current_room = kitchen

dead = False

while dead != True:
	print("\n")
	current_room.get_details()

	inhabitant = current_room.get_character()

	if inhabitant is not None:
		inhabitant.describe()

	command = input("> ")

	if command in ["east","west","north","south"]:
		# move in that direction
		current_room = current_room.move(command)
	elif command == "talk":
		# talk with the inhabitant - check if one is there or not
		if current_room.get_character() is not None:
			inhabitant.talk()
		else:
			print("There is no one here to talk with!")
	elif command == "fight":
		if current_room.get_character() is not None:
			print("What will you fight with?")
			fight_with = input()
			# Try to fight
			if inhabitant.fight(fight_with) == True:
				# What happens if you win
				print("You survived!")
			else:
				# What happens if you lose
				print("Game Over!")
				dead = True
		else:
			print("This is no one here to fight!")


	