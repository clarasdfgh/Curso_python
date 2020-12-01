#utiliza esta funcion para saber si es primo o no
def esprimo(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True
        
def filtrarprimos(numeros):
	primos = []
	
	for x in numeros:
		if esprimo(x):
			primos.append(x)

	return primos

num = [1,2,3,4,5,6,7,8,9,10,11]

print(filtrarprimos(num))

