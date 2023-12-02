# PARTE 1
#
# Proceso:
# 1. Leer archivo de texto.
# 2. Procesar cada linea dentro del archivo.
# 3. Extraemos el primer digito de la linea.
# 4. Extraemos el ultimo digito de la linea.
# 5. Concatanemos ambos digitos.
# 6. Sumamos digitos encontrados.
#
# NOTA: si un dia, solo tiene un digito, este debe ser doblado.
#
# Ejemplo:
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
#
# Los valores de calibracion serian: 12, 38, 15, and 77.
# Y al sumarlos producen un total de 142.
#
# PARTE 2
#
# Hay que tomar en consideracion a los digitos escritos en texto:
# one, two, three, four, five, six, seven, eight, and nine
#
# Modificacion al proceso de PARTE 1
# 3. Buscar de forma directa (izquierda a derecha), el primera digito.
# 4. Buscar de forma inversa (derecha a izquierda), el segundo y ultimo digito.
#
# Ejemplo:
#
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# Los valores de calibracion serian: 29, 83, 13, 24, 42, 14, and 76.
# Y al sumarlos producen un total de 281.


import os

CURRENT_PATH = os.path.dirname(__file__)
INPUT_FILE = "data/input.txt"
INPUT_FILEPATH = os.path.join(CURRENT_PATH, INPUT_FILE)

WRITTEN_DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open(INPUT_FILEPATH, mode="r", encoding="utf-8") as f:
    values = []
    for line in f.readlines():
        digits = []
        # first search
        word = ""
        for char in line:
            word += char
            if char.isdigit():
                digits.append(char)
                break
            elif len(word) >= 3:
                for key, value in WRITTEN_DIGITS.items():
                    if key in word:
                        digits.append(value)
                        break
                else:
                    continue  # only executed if the inner loop did NOT break
                break
        # second search
        reversed_word = ""
        for char in reversed(line):
            reversed_word += char
            if char.isdigit():
                digits.append(char)
                break
            elif len(reversed_word) >= 3:
                word = "".join(reversed_word[::-1])
                for key, value in WRITTEN_DIGITS.items():
                    if key in word:
                        digits.append(value)
                        break
                else:
                    continue  # only executed if the inner loop did NOT break
                break
        if len(digits) > 1:
            value = digits[0] + digits[-1]  # "".join(digits)
        elif len(digits) == 1:
            value = digits[0] * 2
        else:
            raise RuntimeError("Digits array is empty!")
        values.append(int(value))
    print("Sum of values:", sum(values))
