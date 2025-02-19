"""
Instrucciones

Tu objetivo hoy es construir un "Juego elige tu propia aventura". Utilizando lo que has aprendido en las lecciones de hoy, construirás una versión muy simple de este tipo de juego de texto.

Usa el diagrama de flujo enlazado aquí para crear la lógica del juego.
https://acortar.link/KGa64P

¡Una vez que hayas completado el proyecto, siempre puedes ampliar el juego y hacerlo más interesante!

"""
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bienvenido a la Isla del Tesoro.")
print("Tu mision es encontrar el tesoro.")

lado = input("Estas en una encrucijada. ¿A donde quieres ir? ¿izquierda o derecha? ").lower()
if lado == "izquierda":
    accion = input("Llegas a un lago. ¿Quieres nadar o esperar? ").lower()
    if accion == "esperar":
        puerta = input("Te subes a un bote y llegas a una isla. Hay una casa con 3 puertas. ¿Cuál eliges? roja, amarilla o azul? ").lower()
        if puerta == "amarilla":
            print("¡Enhorabuena! ¡Encontraste el tesoro!")
        elif puerta == 'azul':
            print("Eres comido por osos. Fin del juego.")
        elif puerta == 'roja':
            print("¡Te quemas en llamas! Fin del juego.")
        else:
            print("Decisión incorrecta. Fin del juego.")
    elif accion == "nadar":
        print("Un monstruo te come. Fin del juego.")
    else:
        print("Decisión incorrecta. Fin del juego.")
elif lado == "derecha":
    print("Te caes en un agujero y mueres. Fin del juego.")
else:
    print("Decisión incorrecta. Fin del juego.")

                     