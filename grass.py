import random

class Grass():
	def __init__(self):
		pass

	def enter(self):
		a = random.randint(1,10)
		if a == 1:
			return True
		else:
			return False

g = Grass()
print(g.enter())
