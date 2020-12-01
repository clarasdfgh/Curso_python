def factorial(n):
	if n < 0:
		return "Error"

	factorial = 1
	
	for i in range(1,n+1):
		factorial = factorial*i
   
	return factorial

def esprimo(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True
        

