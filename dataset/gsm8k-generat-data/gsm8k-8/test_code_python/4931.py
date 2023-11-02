def solution():
    # Define the initial number of seeds
    initial_seeds = 300

    # Calculate the number of seeds that land in water and die
    water_death = (1/3) * initial_seeds

    # Calculate the number of seeds that are eaten by insects
    insect_eaten = (1/6) * initial_seeds

    # Calculate the remaining seeds after water and insect deaths
    remaining_seeds = initial_seeds - water_death - insect_eaten

    # Calculate the number of surviving seeds after sprouting and being eaten
    surviving_seeds = (1/2) * remaining_seeds

    result = surviving_seeds
    return result

print(solution())