class Room():

	def __init__(self, room_name):
		self.name = room_name
		self.description = None
		self.character = None
		self.linked_rooms = {}

	# Getters and Setters
	def set_description(self, room_description):
		self.description = room_description

	def get_description(self):
		return self.description

	def set_name(self, room_name):
		self.name = room_name

	def get_name(self):
		return self.name

	def set_character(self, new_character):
		self.character = new_character

	def get_character(self):
		return self.character

	def describe(self):
		print(self.description)

	# Add linked room method
	def link_room(self, room_to_link, direction):
		self.linked_rooms[direction] = room_to_link

	def get_details(self):
		print("The " + self.name)
		print("-------------------")
		print(self.description)
		for direction in self.linked_rooms:
			room = self.linked_rooms[direction]
			print("The " + room.get_name() + " is " + direction)

	def move(self, direction):
		if direction in self.linked_rooms:
			return self.linked_rooms[direction]
		else:
			print("Sorry, you can't go that way")
			return self

