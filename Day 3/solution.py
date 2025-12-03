def part_one() -> None:
    """
    Si, esto es un 0(2n) desde un input de 200 líneas, bien
    ineficiente.

    Tomamos dos índices, desde 0 y 1 y ambos llegan hasta n (que es
    la longitud de una linea del input). Iteramos sobre toda la linea
    y, como en ese momento aun siguen siendo strings, podemos concatenar
    y luego convertir a string para cada par de números en la línea.
    Lo comparamos contra un valor 'largest'. ¿Es más grande que ese valor?
    ¿Si?, entonces lo cambiamos y seguimos. ¿No?, solo seguimos.
    Al final solo añadimos ese valor a joltage y asi en cada linea.
    """

    joltage = 0
    with open("Day 3/input.txt", "r") as input:
        for line in input:
            largest = 0
            batteries = line.strip()
            for i in range(len(batteries)):
                for j in range(i + 1, len(batteries)):
                    values = int(batteries[i] + batteries[j])
                    if values > largest:
                        largest = values
            joltage += largest

    print(f"Total joltage is {joltage}")


def part_two() -> None:
    """
    Nuevamente, a revisar todo el input, por que why not?
    Aquí la diferencia es que es partir desde una cadena
    de 12 caracteres e ir revisando hacia adelante. Igual
    como en el caso anterior se va cambiando y continuando
    en la revisión hasta obtener el valor general de 'joltage'
    para la cadena.
    """
    joltage = 0
    largest_bank = ""
    with open("Day 3/input.txt") as input:
        for line in input:
            batteries = line.strip()
            # De momento, el más grande.
            largest_bank = batteries[:12]
            # para revisar del 11 en adelante
            for battery in range(12, len(batteries)):
                index = batteries[battery]
                # que serían los otros 12 en adelante.
                for i in range(12):
                    # la idea sería ir uniendo las cadenas (o números ya convertidos)
                    # desde [0->i] + [i+1:12] + index. Pues, si hay un 811111111111119
                    # entonces seria revisar del índice 0 al 11, luego los intermedios
                    # y finalmente el índice (que sería la posición 12 realemnte).
                    temp = largest_bank[0:i] + largest_bank[i + 1 : 12] + index
                    # y ya finalmente se convierte a para obtener el valor.
                    if int(temp) > int(largest_bank):
                        largest_bank = temp
                        break
            joltage += int(largest_bank)
    print(f"Total joltage for largest_bank is {joltage}")


if __name__ == "__main__":
    part_one()
    part_two()
