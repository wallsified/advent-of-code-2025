def find_accessible_in_grid(grid) -> (int, [str]):
    """
    En ambos casos tenemos que revisar toda la "cuadrícula" para revisar
    lo que es accesible desde las direcciones adyacentes a la posición en
    donde estamos.

    Como ésta función ayuda para ambas partes del problema, tiene sentido
    que al mismo tiempo regrese tanto el valor de los rollos de papel
    a los que se puede acceder como la cuadrícula de adyacencia, y solo
    ocupar lo nececesario en cada caso.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    accessible_grid = []
    accessible_rolls = 0

    # Nótese que falta el (0,0) intencionalmente.
    adyacent_directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    # Vamos a darle toda la vuelta a la cuadrícula.
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "@":
                # Encontramos un rollo, ¿podemos moverlo?
                adjacent_rolls = 0
                for index_i, index_j in adyacent_directions:
                    # Para saberlo hay que revisar las direcciones adyacentes
                    # a partir de nuestra posición.
                    next_i, next_j = i + index_i, j + index_j
                    # Aquí tiene que ser <= para considerar que iniciamos en 0
                    # en ambos índices.
                    if 0 <= next_i < rows and 0 <= next_j < cols:
                        if grid[next_i][next_j] == "@":
                            adjacent_rolls += 1
                # Aqui es estricto, fewer than. Que en la vida real tiene algo
                # de sentido por que serian los movimientos lógicos de un
                # montacargas. También empezamos a formar la cuadrícula de
                # adyacencia en este punto.
                if adjacent_rolls < 4:
                    accessible_grid.append((i, j))
                    accessible_rolls += 1

    return accessible_grid, accessible_rolls


def part_one() -> None:
    """
    La función auxiliar resuelve toda la primera
    parte. Solo ocupamos lo segundo que ésta regresa
    pues no se necesita una cuadrícula de adyacencia
    posteriormente.
    """
    with open("input.txt", "r") as input:
        grid = [list(line.strip()) for line in input.readlines()]
        _, accessible_rolls = find_accessible_in_grid(grid)
    print(f"\nTotal of accesible rolls is {accessible_rolls}")


def part_two() -> None:
    """
    Aquí ocupamos la otra parte del regreso de la función auxiliar,
    pero es necesario estar cambiando la cuadrícula accesible hasta
    que no haya nada accesible. Cuando esto pasa significa que ya
    retiramos todos los rollos posibles.
    """
    total_removed = 0
    with open("input.txt", "r") as input:
        grid = [list(line.strip()) for line in input.readlines()]
        accesibble_grid, _ = find_accessible_in_grid(grid)
    while accesibble_grid:
        for i, j in accesibble_grid:
            grid[i][j] = "."
        total_removed += len(accesibble_grid)
        accesibble_grid, _ = find_accessible_in_grid(grid)
    print(f"Total rolls that can be removed: {total_removed}")


if __name__ == "__main__":
    part_one()
    part_two()
