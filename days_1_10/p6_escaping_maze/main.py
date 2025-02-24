"""
link=https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

Reeborg estaba explorando un laberinto oscuro y la batería de su linterna se agotó.

Escriba un programa usando una declaración if/elif/else para que Reeborg pueda encontrar la salida. El secreto es hacer que Reeborg siga el borde derecho del laberinto, girando a la derecha si puede, siguiendo recto si no puede girar a la derecha o girando a la izquierda como último recurso.

Lo que necesitas saber
Las funciones move() y turn_left().
Ya sea la prueba front_is_clear() o wall_in_front(), right_is_clear() o wall_on_right() y at_goal().
Cómo utilizar un bucle while y declaraciones if/elif/else.
Puede resultar útil saber cómo utilizar la negación de una prueba (no en Python).

Un robot ubicado en (x, y) = (1, 3) no lleva objetos.

Meta a lograr:
La posición final del robot debe ser (x, y) = (6, 4)
"""
def turn_right():
    # Función para girar a la derecha
    turn_left()
    turn_left()
    turn_left()

def solve_maze():
    while not at_goal():
        # Si el camino de frente está libre, avanza
        if front_is_clear():
            move()
        else:
            # Si hay una pared, gira a la derecha y prueba
            turn_right()
            if front_is_clear():
                move()
            else:
                # Si no hay camino a la derecha, gira a la izquierda
                turn_left()
                if front_is_clear():
                    move()
                else:
                    # Si sigue bloqueado, gira a la izquierda nuevamente
                    turn_left()
                    if front_is_clear():
                        move()
                    else:
                        # Si sigue bloqueado, gira a la izquierda una vez más
                        turn_left()

#Función principal
solve_maze()
