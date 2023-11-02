def solution():
    # Find the number of cows on the farm
    pigs = 10
    cows = 2 * pigs - 3
    goats = cows + 6
    total_animals = pigs + cows + goats

    result = total_animals
    return result

print(solution())