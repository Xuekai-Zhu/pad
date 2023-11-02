def solution():
    num_pigs = 10

    # Calculate the number of cows
    num_cows = 2*num_pigs - 3

    # Calculate the number of goats
    num_goats = num_cows + 6

    # Calculate the total number of animals on the farm
    total_animals = num_pigs + num_cows + num_goats
    result = total_animals
    return result

print(solution())