from character import Enemy

dave = Enemy("Dave","A very smelly Zombie")

dave.describe()

dave.set_weakness("cheese")

# Add some conversation
dave.set_conversation("Yo, what's up?")

# Trigger a conversation
dave.talk()

print("What will you fight with?")
fight_with = input()

# Try to fight
dave.fight(fight_with)