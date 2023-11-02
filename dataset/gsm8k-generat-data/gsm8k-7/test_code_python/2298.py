def solution():
    num_seeds = 10
    num_pots = 4
    seeds_per_pot = 3
    
    # Calculate the total number of seeds that will be used for the first 3 pots
    seeds_used = (num_pots - 1) * seeds_per_pot
    
    # Calculate the remaining number of seeds for the fourth pot
    remaining_seeds = num_seeds - seeds_used
    
    # Calculate the number of seeds that will be planted in the fourth pot
    seeds_in_fourth_pot = remaining_seeds % seeds_per_pot
    result = seeds_in_fourth_pot
    return result

print(solution())