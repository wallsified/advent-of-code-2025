def part_one() -> None:
    """
    La lógica que yo entendi aquí fue que cada entrada puede ser como una una
    mini-lista, con lista[0] la direccion (L o R) y luego la distancia.

    Luego, en el reto dice esto:
        'So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19.
        After that, a rotation of L19 would cause it to point at 0.'
    que seria algo como "Si es R, sumas la posición mas la distancia y si es L restas distancia de la posición"

    Pero el truco está en que la contraseña es realmente la cantidad de 0 a los que uno termina apuntando
    tras cada rotación. Y como estamos con valores de 0 a 99, y no es que magicamente lleguemos a un -5 o
    parecido, si hacemos un mod 100 de las operaciones de arriba resolvemos ese problema para saber
    realmente en que posición estamos tras cada rotación.
    """

    position = 50  # Se menciona que se inicia de esta posición
    password = 0  # supongo que algo como contador_de_ceros igual funciona, pero al final signfican lo mismo.
    with open("Day 1/input.txt", "r") as input:
        for rotation in input:
            rotation = rotation.strip()
            if not rotation:
                continue  # para los EOF

            direction = rotation[0]
            distance = int(rotation[1:])

            if direction == "L":
                position = (position - distance) % 100
            elif direction == "R":
                position = (position + distance) % 100

            if position == 0:
                password += 1
    print(f"Password is: {password}")


def part_two() -> None:
    """
    Aqui compartimos la misma lógica de los mods y las posiciones, pero ahora tenemos que considerar
    todos los clicks que lleven a la posición 0, ya sea antes o después de las rotaciones (y no al final
    que era lo que haciamos en el paso anterior).

    Entonces lo que hacemos es que si nos da a una posición mayor a 100 es que ya se hizo ese click, entonces
    dividimos entre +/- 100 para saber la cantidad de rotaciones completas.

    De ahi es la misma lógica del módulo de la parte anterior.
    """
    position = 50
    password = 0
    with open("Day 1/input.txt", "r") as input:
        for rotation in input:
            direction = rotation[0]
            distance = int(rotation[1:])

            if not rotation:
                continue  # para los EOF

            if direction == "R":
                position = position + distance
                if position >= 100:
                    password += position // 100
            else:
                prev = position
                position = position - distance
                if position <= 0:
                    password += position // -100 + 1
                    if prev == 0:
                        password -= 1

            position = position % 100

    print(f"Password is: {password}")


if __name__ == "__main__":
    part_one()
    part_two()
