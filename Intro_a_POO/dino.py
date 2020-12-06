class Dinosaurio:
	def __init__(self, color, especie, altura):
		self.color = color
		self.especie = especie
		self.altura = int(altura)

	def rugir(self):
		print("RAWR!!")
		
	def crecer(self, crecimiento):
		self.altura = self.altura + crecimiento
		
dino = Dinosaurio("Rojo", "T-Rex", 4)

dino.rugir()
dino.crecer(1)

print(dino.color)
print(dino.especie)
print(dino.altura)
