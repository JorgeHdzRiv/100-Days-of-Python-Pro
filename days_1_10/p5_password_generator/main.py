"""
Programa para generar passwords

El programa preguntará:

¿Cuántas letras te gustaría en tu contraseña?
¿Cuántos símbolos te gustaría?
¿Cuántos números te gustaría?
El objetivo es tomar las entradas del usuario a estas preguntas y luego generar una contraseña aleatoria. 
Usa tu conocimiento sobre las listas y los bucles de Python para completar el desafío.

Version facil:
Genera la contraseña en secuencia. Letras, luego símbolos, luego números. Si el usuario quiere

4 letras 2 símbolos y 3 números entonces la contraseña podría verse así:

fgdx$*924

Puedes ver que todas las letras están juntas. Todos los símbolos están juntos y todos los números siguen el mismo orden. 
Intenta resolver este problema primero.

Version dificil:
Cuando hayas completado la versión fácil, estarás listo para afrontar la versión difícil. En la versión avanzada de este proyecto, 
la contraseña final no sigue un patrón. Entonces el ejemplo anterior podría verse así:

x$d24g*f9

Y cada vez que generes una contraseña, las posiciones de los símbolos, los números y las letras son diferentes. 
Esto hará que la contraseña sea más difícil de descifrar para los hackers.

"""
import random
minisculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']       
mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letras = minisculas + mayusculas

# Version facil
print("Bienvenido al generador de contraseñas")
n_letras = int(input("¿Cuántas letras te gustaría en tu contraseña?: \n"))
n_simbolos = int(input("¿Cuántos símbolos te gustaría?: \n"))
n_numeros = int(input("¿Cuántos números te gustaría?: \n"))
password = ""
for letra in range(n_letras):
    password += random.choice(letras)
for simbolo in range(n_simbolos):
    password += random.choice(simbolos)
for numero in range(n_numeros):
    password += random.choice(numeros)

print(f'\nPassword generada facil: {password}\n')

# Version dificil
password = list(password)
random.shuffle(password)
password = "".join(password)
print(f'Password generada dificil: {password}')



