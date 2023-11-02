def solution():
    """Each dandelion produces 300 seeds. 1/3rd of the seeds land in water and die. 1/6 of the starting number are eaten by insects. Half the remainder sprout and are immediately eaten. How many dandelions survive long enough to flower?"""
    initial_seeds = 300
    seeds_in_water = initial_seeds / 3
    seeds_eaten_by_insects = initial_seeds / 6
    remaining_seeds = initial_seeds - seeds_in_water - seeds_eaten_by_insects
    sprouted_seeds_eaten = remaining_seeds / 2
    final_seeds = remaining_seeds - sprouted_seeds_eaten
    result = final_seeds / initial_seeds
    return result

print(solution())