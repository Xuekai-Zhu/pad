def solution():
    # Find the number of zebras Mr. Bodhi has
    num_foxes = 15
    num_zebras = 3 * num_foxes

    # Find the number of sheep needed to balance the yacht
    num_cows = 20
    total_animals = num_cows + num_foxes + num_zebras
    num_sheep = 100 - total_animals
    result = num_sheep
    return result

print(solution())