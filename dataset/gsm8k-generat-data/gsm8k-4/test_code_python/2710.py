def solution():
    """On a farm, there are 2 cows, 3 pigs, and 6 goats. The farmer planned on adding 3 cows, 5 pigs, and 2 goats. How many animals will there be on the farm?"""
    # Define the initial number of cows, pigs, and goats
    initial_cows = 2
    initial_pigs = 3
    initial_goats = 6

    # Define the number of cows, pigs, and goats to be added
    add_cows = 3
    add_pigs = 5
    add_goats = 2

    # Calculate the new number of cows, pigs, and goats
    total_cows = initial_cows + add_cows
    total_pigs = initial_pigs + add_pigs
    total_goats = initial_goats + add_goats

    # Calculate the total number of animals on the farm
    total_animals = total_cows + total_pigs + total_goats

    # Return the result
    result = total_animals
    return result

print(solution())