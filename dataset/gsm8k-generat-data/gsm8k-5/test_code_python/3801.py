def solution():
    lions_safari = 100
    snakes_safari = lions_safari / 2
    giraffes_safari = snakes_safari - 10
    lions_savanna = lions_safari * 2
    snakes_savanna = snakes_safari * 3
    giraffes_savanna = giraffes_safari + 20

    total_animals = lions_savanna + snakes_savanna + giraffes_savanna
    result = total_animals
    return result

print(solution())