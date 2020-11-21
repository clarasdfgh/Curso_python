#no borres esto para que podamos evaluarte
usuarios = {"juanito":1245613, "eva":9109201, "santi":9239367}
usuario = input()

try:
    print(usuarios[usuario])
except:
    print("no encontrado")
