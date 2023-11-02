def solution():
    # Define the initial number of animals
    cows = 2
    pigs = 3
    goats = 6

    # Add the planned number of animals
    cows += 3
    pigs += 5
    goats += 2

    # Calculate the total number of animals
    total_animals = cows + pigs + goats

    result = total_animals
    return result

print(solution())