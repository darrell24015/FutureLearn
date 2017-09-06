from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate decorations.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Testing the get_details() method
# dining_hall.get_details()
# kitchen.get_details()
# ballroom.get_details()

current_room = kitchen

while True:
	print("\n")
	current_room.get_details()
	command = input("> ")
	current_room = current_room.move(command)