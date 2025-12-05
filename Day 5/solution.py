def part_one() -> None:
    fresh_ranges = []
    available_ingredients = []
    fresh_counter = 0

    with open("input.txt", "r") as input:
        database = input.read().strip()
        # El input viene separado por un doble salto de linea, entonces
        # simplemente se divide en dos partes: los rangos y los IDs.
        parts = database.split("\n\n")
        ranges_section = parts[0]
        ids_section = parts[1]

        # Consideramos los rangos como tuplas en una lista de, pues rangos.
        for line in ranges_section.strip().split("\n"):
            start, end = map(int, line.split("-"))
            fresh_ranges.append((start, end))

        # IDs en texto a buscar convertidos en ints y a una lista.
        for line in ids_section.strip().split("\n"):
            available_ingredients.append(int(line))

        # Y como la eficiencia se fue de sabático, comparamos cada
        # ID en la lista de rangos de frescura, uno a la vez, en cada
        # rango.
        for ingredient_id in available_ingredients:
            is_fresh = False
            # aqui es donde la eficiencia se va al traste. Supongo
            # que modificar para hacer algo como ranges.next() y
            # asi iterar dos cosas a la vez sería más rápido.
            # pero habría que ordenar y/o mezclar los rangos.
            for start, end in fresh_ranges:
                if start <= ingredient_id <= end:
                    is_fresh = True
                    break
            if is_fresh:
                fresh_counter += 1
    print(f"Total fresh ingredients is {fresh_counter}")


def part_two() -> None:
    fresh_ranges = []
    # fresh_ingredient_ids = set()

    with open("input.txt", "r") as input:
        database = input.read().strip()
        parts = database.split("\n\n")
        ranges_section = parts[0]

        for line in ranges_section.strip().split("\n"):
            start, end = map(int, line.split("-"))
            fresh_ranges.append((start, end))

        # Si tienes la ram suficiente, en teoria con eso sale.
        # De hecho a mi me salio una vez y luego ya no me dejo.
        # Ni idea del por que.
        # for start, end in fresh_ranges:
        #     for ingredient_id in range(start, end + 1):
        #         fresh_ingredient_ids.add(ingredient_id)

    fresh_ranges.sort()
    merged_ranges = []
    for start, end in fresh_ranges:
        # checamos si el nuevo rango empieza antes o justo despues del ultimo rango mezclado
        # si si se actualizan los rangos y si no solo se añade un nuevo rango independiente.
        if merged_ranges and start <= merged_ranges[-1][1] + 1:
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))
        else:
            merged_ranges.append((start, end))

    total_fresh_ingredients = sum(end - start + 1 for start, end in merged_ranges)

    print(f"Total unique fresh ingredient IDs: {total_fresh_ingredients}")
    # print(f"Total unique fresh ingredient IDs: {len(fresh_ingredient_ids)}")


if __name__ == "__main__":
    part_one()
    part_two()
