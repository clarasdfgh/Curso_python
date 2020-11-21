#no modifiques esto para que te podamos evaluar
n = int(input("Numero: "))

i = 2
primo = True

for i in range(i,n,1) :
	if n % i == 0 :
		primo =  False
	if primo == False :
		break

if primo :
	print("{}es primo".format(n))
else :
	print("{}no es primo".format(n))
		
