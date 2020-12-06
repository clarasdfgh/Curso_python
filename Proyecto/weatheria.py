import stormymod
import swowpy

ciudades = []
n        = 10
api_key  = "fd9783118e7563a98a7f7b3f2acd4d7b"

for i in range(0, n): 
	ciudad = input("Inserte ciudad: ") 

	ciudades.append(ciudad)
	

for i in range(0, n):
	try:
		mycity = swowpy.Swowpy(api_key,ciudades[i])

		print("\n",ciudades[i])
		print("\tTiempo: ", mycity.current_weather())
		print("\tTemperatura: ", round(mycity.temperature()-273.15, 2), "ºC")	#No conseguí que funcionara el parámetro Celsius
		print("\tPresión: ", mycity.pressure(), "Pa")
		stormymod.stormy(mycity)
		
	except:
  		print("\tError en la lectura") 


