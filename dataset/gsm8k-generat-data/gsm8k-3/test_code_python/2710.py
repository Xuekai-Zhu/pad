def solution():
    """On a farm, there are 2 cows, 3 pigs, and 6 goats. The farmer planned on adding 3 cows, 5 pigs, and 2 goats. How many animals will there be on the farm?"""
    # Define the initial number of each animal on the farm
    initial_cows = 2
    initial_pigs = 3
    initial_goats = 6

    # Define the number of each animal the farmer plans to add
    added_cows = 3
    added_pigs = 5
    added_goats = 2

    # Calculate the total number of each animal on the farm after the additions
    total_cows = initial_cows + added_cows
    total_pigs = initial_pigs + added_pigs
    total_goats = initial_goats + added_goats

    # Calculate the total number of animals on the farm
    total_animals = total_cows + total_pigs + total_goats

    # Display the total number of animals on the farm
    result = total_animals
    return result

print(solution())