usuarios = ("franky", "robin", "brook")
contrasenias = ("123", "abc", "h4h4")

user = input("Usuario: ")
passwd = input("Contraseña: ")

coincide = False
i = 0

while i < len(usuarios):
	if user == usuarios[i] and passwd == contrasenias[i] :
		coincide = True
		print("Login correcto")
		break
	else :
		i += 1
	
	if i == len(usuarios) :
		print("Login incorrecto")
		break

print("---")
	
