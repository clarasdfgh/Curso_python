import swowpy

def stormy(city):
	presion = city.pressure()
	
	if(presion < 990):
		print("AVISO POR TORMENTA")
