def solution():
    # Calculate the number of ducks
    ducks = 20 * 1.5

    # Calculate the total number of cows and ducks
    cows_and_ducks = 20 + ducks

    # Calculate the number of pigs
    pigs = cows_and_ducks // 5

    # Calculate the total number of animals
    total_animals = cows_and_ducks + pigs
    result = total_animals
    return result

print(solution())