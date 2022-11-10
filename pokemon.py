from enum import Enum

class Pokemon:
	def __init__(self, name, pkmn_type, gender=None, stats=None):
		self.name = name
		self.pkmn_type = pkmn_type
		self.stats = stats
		self.gender = gender

	def __str__(self):
		gender = None
		if (self.gender == PokemonGender.MALE):
			gender = '♂'
		else:
			gender = '♀'
		return self.name + " " + str(self.pkmn_type) + " " + gender

	def emote(self):
		if(self.gender == PokemonGender.MALE):
			print("squee!")
		else:
			print("Squee!")

class PokemonType(Enum):
	FIGHTING=1
	FIRE = 2
	WATER = 3
	GRASS = 4
	ELECTRIC = 5
	PSY = 6

class PokemonGender(Enum):
	FEMALE=1
	MALE=2
