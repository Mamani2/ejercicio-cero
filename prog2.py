# Juego de adivinar el numero

import random

#juego de adivinanza
numero_secreto=random.randint(1,20)
intentos = 0

print("estoy pensando en un numero entre 1  y 20. !adivinalo!")
 
while True:
    intento = int(input("introduce tu numero: "))
    intentos +=1
    
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta otra vez.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta otra vez.")
    else:
        print(f"felicidades! acertaste en {intentos}.")
        break    