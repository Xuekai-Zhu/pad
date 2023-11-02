def solution():
    # Starting number of animals
    cows = 2
    pigs = 3
    goats = 6

    # Number of animals being added
    new_cows = 3
    new_pigs = 5
    new_goats = 2

    # Total number of animals after addition
    total_cows = cows + new_cows
    total_pigs = pigs + new_pigs
    total_goats = goats + new_goats

    # Sum of all animals
    total_animals = total_cows + total_pigs + total_goats
    result = total_animals
    return result

print(solution())