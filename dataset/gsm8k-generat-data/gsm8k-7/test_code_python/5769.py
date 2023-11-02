def solution():
    num_cows = 24
    num_sheep = 7
    total_animals = num_cows + num_sheep

    num_groups = 3
    animals_per_group = 48

    # Calculate the total number of animals that will be transported
    total_transport = num_groups * animals_per_group

    # Calculate the number of goats owned by subtracting the known animals from the total
    num_goats = total_transport - total_animals
    result = num_goats
    return result

print(solution())