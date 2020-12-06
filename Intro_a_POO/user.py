class User:
	def __init__(self, nombre, apellidos):
		self.nombre = nombre
		self.apellidos = apellidos

	def postear(self, mensaje):
		print(mensaje)

usuario = User("juanito", "perez")
 
usuario.postear("Hola Mundo")

print(usuario.nombre)
print(usuario.apellidos)
