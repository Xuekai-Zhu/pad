def solution():
    """On a farm, there are 2 cows, 3 pigs, and 6 goats. The farmer planned on adding 3 cows, 5 pigs, and 2 goats. How many animals will there be on the farm?"""
    initial_cows = 2
    initial_pigs = 3
    initial_goats = 6
    added_cows = 3
    added_pigs = 5
    added_goats = 2
    total_cows = initial_cows + added_cows
    total_pigs = initial_pigs + added_pigs
    total_goats = initial_goats + added_goats
    total_animals = total_cows + total_pigs + total_goats
    result = total_animals
    return result

print(solution())