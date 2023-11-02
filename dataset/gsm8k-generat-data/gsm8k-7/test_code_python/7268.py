def solution():
    num_cows = 20
    num_foxes = 15
    num_zebras = 3 * num_foxes
    total_animals = 100

    # Calculate the current total number of animals in the yacht
    current_total_animals = num_cows + num_foxes + num_zebras

    # Calculate the number of sheep that Mr. Bodhi needs to add to balance the yacht
    num_sheep = total_animals - current_total_animals
    result = num_sheep
    return result

print(solution())