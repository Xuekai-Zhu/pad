def solution():
    pigs = 10  # Hannah's family has 10 pigs
    cows = 2 * pigs - 3  # Hannah's family has 3 fewer than twice as many cows as pigs
    goats = cows + 6  # Hannah's family has 6 more goats than cows

    # Calculate the total number of animals on the farm
    total_animals = pigs + cows + goats
    result = total_animals
    return result

print(solution())