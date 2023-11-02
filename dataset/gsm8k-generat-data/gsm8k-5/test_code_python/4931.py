def solution():
    starting_seeds = 300  # Each dandelion produces 300 seeds
    water_death_rate = 1/3  # 1/3 of the seeds land in water and die
    insect_eaten_rate = 1/6  # 1/6 of the starting number are eaten by insects

    # Calculate the number of seeds that survive after water and insect damage
    surviving_seeds = starting_seeds - (starting_seeds * water_death_rate) - (starting_seeds * insect_eaten_rate)

    # Calculate the number of seeds that sprout and are immediately eaten
    sprouted_seeds = surviving_seeds / 2
    eaten_seeds = sprouted_seeds

    # Calculate the final number of surviving dandelions
    surviving_dandelions = (surviving_seeds - sprouted_seeds) - eaten_seeds
    result = surviving_dandelions
    return result

print(solution())