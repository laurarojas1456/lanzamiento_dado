# Programa para simular el lanzamiento de un dado

import random

print("------------------------------------------------------")
print("------------- LANZAMIENTO DE UN DADO -----------------")
print("------------------------------------------------------")

# input

# processing
d = random.randint(1,6)

if (d==1):
    rta = "UNO"
elif (d==2):
    rta = "DOS"
elif (d==3):
    rta = "TRES"
elif (d==4):
    rta = "CUATRP"
elif (d==5):
    rta ="CINCO"
elif (d==6):
    rta ="SEIS"
else:
    rta= "NO ES LA CARA DE UN DADO"

# output
print("El dado cayó en " + str(rta))