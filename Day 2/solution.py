def part_one_helper(num):
    num_str = str(num)
    length = len(num_str)

    # Debemos buscar patrones de números que se repitan dos veces, entonces
    # números como 22 o 4444 son inválidos. Los IDs de longitud impar no entrarian
    # por que no se pueden dividir entre dos para encontrar patrones dobles.
    if length % 2 != 0:
        return False

    # Y luego se revisa la mitad izquierda y la derecha para revisar si
    # son mitadas iguales o no.
    half = length // 2
    return num_str[:half] == num_str[half:]


def part_two_helper(num):
    num_str = str(num)
    length = len(num_str)

    # Debemos buscar patrones de números que se repitan al menos dos veces, entonces
    # números como 22, 123123, 1111111, se descartan. Eso hace que lo mas que puede
    # medir un id es su longitud/2, y que sea divisible entre si.
    for pattern_length in range(1, (length // 2 + 1)):
        if length % pattern_length == 0:
            pattern = num_str[
                :pattern_length
            ]  # Esto lo que hace crea los patrones de numeros, como 22, 123, etc.
            # Aqui revisamos si el ID esta compuesto de su mismo patron en base a lo anterior.
            if pattern * (length // pattern_length) == num_str:
                return True

    return False


def part_one():
    ranges = []
    invalid_ids = []
    total_sum = 0

    with open("Day 2/input.txt", "r") as input:
        input = input.read()
        for range_str in input.strip().split(","):
            start, end = map(int, range_str.split("-"))
            ranges.append((start, end))

    for start, end in ranges:
        for num in range(start, end + 1):
            if part_one_helper(num):
                invalid_ids.append(num)
                total_sum += num

    print(f"Total sum of invalid IDs: {total_sum}")
    print(f"Total invalid IDs found: {len(invalid_ids)}")


def part_two():
    ranges = []
    invalid_ids = []
    total_sum = 0

    with open("Day 2/input.txt", "r") as input:
        input = input.read()
        for range_str in input.strip().split(","):
            start, end = map(int, range_str.split("-"))
            ranges.append((start, end))

    for start, end in ranges:
        for num in range(start, end + 1):
            if part_two_helper(num):
                invalid_ids.append(num)
                total_sum += num

    print(f"Total sum of invalid IDs: {total_sum}")
    print(f"Total invalid IDs found: {len(invalid_ids)}")


if __name__ == "__main__":
    part_one()
    part_two()
