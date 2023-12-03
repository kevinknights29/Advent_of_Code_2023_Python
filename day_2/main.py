# PARTE 1
#
# Proceso:
# 1. Leer archivo de texto.
# 2. Procesar cada linea dentro del archivo.
# 3. Extraemos el id del juego.
#   Intuyo oportunidad de split por ":".
# 4. Extraemos la configuracion de cada ronda.
#   Intuyo oportunidad de split por ";".
# 5. Extraemos la cantidad de cubos por color.
#   Intuyo oportunidad de split por ",".
# 6. Validamos si algun numero excede la configuracion.
# 7. Si no excede agregamos el id del juego a una lista.
# 8. Sumamos la lista de ids.
#
# NOTA: si un dia, solo tiene un digito, este debe ser doblado.
#
# Ejemplo:
#
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
#
# Se desea saber cuantos juegos seran posibles con la siguiente configuracion
#     12 red cubes, 13 green cubes, and 14 blue cubes?
# En el ejemplo, los juegos 1, 2, y 5 hubiesen sido posibles con dicha configuracion.
# No obstante, el juego 3 hubiese sido imposible por los 20 red cubes en un sola ronda;
#     similarmente, el juego 4 hubiese sido imposible por los 15 blue cubes en un sola ronda.
# Si sumamos los IDs de los juegos posibles, obtenemos 8 (1, 2, 5).
#
# PARTE 2
#
# TBD


import os

CURRENT_PATH = os.path.dirname(__file__)
INPUT_FILE = "data/input.txt"
INPUT_FILEPATH = os.path.join(CURRENT_PATH, INPUT_FILE)

GAME_CONFIG = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open(INPUT_FILEPATH, mode="r", encoding="utf-8") as f:
    valid_ids = []
    for line in f.readlines():
        game, rounds = line.split(":", maxsplit=1)
        _, game_id = game.split(" ", maxsplit=1)
        valid_ids.append(int(game_id))
        results = rounds.split(";")
        for result in results:
            result = result.strip()
            colors = result.split(",")
            for color in colors:
                color = color.strip()
                quantity, value = color.split(" ")
                if int(quantity) > GAME_CONFIG[value]:
                    valid_ids.pop()
                    break
                elif int(quantity) < GAME_CONFIG[value]:
                    continue
                else:
                    RuntimeError("Something went wrong...")
            else:
                continue  # only executed if the inner loop did NOT break
            break
    print("Sum: ", sum(valid_ids))
