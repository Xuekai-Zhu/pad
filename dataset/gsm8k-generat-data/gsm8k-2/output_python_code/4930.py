def solution():
    """Each dandelion produces 300 seeds. 1/3rd of the seeds land in water and die. 1/6 of the starting number are eaten by insects. Half the remainder sprout and are immediately eaten. How many dandelions survive long enough to flower?"""
    starting_seeds = 300
    water_death_rate = 1 / 3
    eaten_rate = 1 / 6
    sprout_rate = 0.5
    remaining_seeds_after_water = starting_seeds * (1 - water_death_rate)
    remaining_seeds_after_eaten = remaining_seeds_after_water * (1 - eaten_rate)
    remaining_seeds_after_sprout = remaining_seeds_after_eaten * sprout_rate
    result = remaining_seeds_after_sprout
    return result

print(solution())