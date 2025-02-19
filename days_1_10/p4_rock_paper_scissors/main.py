"""
Instrucciones para el programa
Determinar el ganador de un juego de piedra, papel o tijera
Donde tu eliges la opcion y la computadora elige una opcion aleatoria
Al final se muestra el resultado del juego
"""
import random
piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

opciones = [piedra, papel, tijera]
print("Bienvenido al juego de piedra, papel o tijera")
print("Elige una opcion:")
print("0 para piedra")
print("1 para papel")
print("2 para tijera")
opcion = int(input("Elige una opcion: "))
if opcion >= 3 or opcion < 0:
    print("Opcion invalida")
else:
    print("Tu eleccion:")
    print(opciones[opcion])
    eleccion_pc = random.randint(0, 2)
    print("Elección de la computadora:")
    print(opciones[eleccion_pc])
    
    if opcion == 0 and eleccion_pc == 2:
        print("Ganaste")
    elif eleccion_pc == 0 and opcion == 2:
        print("Perdiste")
    elif opcion == 1 and eleccion_pc == 0:
        print("Ganaste")
    elif eleccion_pc == 1 and opcion == 0:
        print("Perdiste")
    elif opcion == 2 and eleccion_pc == 1:
        print("Ganaste")
    elif eleccion_pc == 2 and opcion == 1:
        print("Perdiste")
    else:
        print("Empate")

