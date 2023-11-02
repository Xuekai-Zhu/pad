def solution():
    starting_seeds = 300
    water_death_rate = 1/3
    insect_eaten_rate = 1/6

    # Calculate the number of seeds that survive water death
    num_seeds_after_water_death = starting_seeds * (1 - water_death_rate)

    # Calculate the number of seeds that survive insect eating
    num_seeds_after_insect_eating = num_seeds_after_water_death * (1 - insect_eaten_rate)

    # Calculate the number of seeds that sprout
    num_sprouted_seeds = num_seeds_after_insect_eating / 2

    # Calculate the number of dandelions that survive long enough to flower
    num_flowering_dandelions = num_sprouted_seeds
    result = num_flowering_dandelions
    return result

print(solution())