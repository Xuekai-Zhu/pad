def solution():
    """On a farm, there are 2 cows, 3 pigs, and 6 goats. The farmer planned on adding 3 cows, 5 pigs, and 2 goats. How many animals will there be on the farm?"""
    current_cows = 2
    current_pigs = 3
    current_goats = 6
    new_cows = 3
    new_pigs = 5
    new_goats = 2
    total_cows = current_cows + new_cows
    total_pigs = current_pigs + new_pigs
    total_goats = current_goats + new_goats
    total_animals = total_cows + total_pigs + total_goats
    result = total_animals
    return result

print(solution())