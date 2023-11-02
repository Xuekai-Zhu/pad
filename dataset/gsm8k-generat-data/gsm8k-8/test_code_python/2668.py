def solution():
    # Define the number of pigs
    pigs = 10

    # Calculate the number of cows
    cows = 2 * pigs - 3

    # Calculate the number of goats
    goats = cows + 6

    # Calculate the total number of animals
    total_animals = pigs + cows + goats

    result = total_animals
    return result

print(solution())