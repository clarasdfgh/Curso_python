#no borres esto para que podamos evaluarte
frase = input()

i = 0
contador = 0

for i in range(len(frase)) :
    if frase[i] == "a" :
        contador += 1

print(contador)        
