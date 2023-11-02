def solution():
    goats = 66
    chickens = 2 * goats  # Twice as many chickens as goats
    ducks = (goats + chickens) / 2  # Half of the total of goats and chickens
    pigs = ducks / 3  # One third of the number of ducks

    # Calculate the difference between the number of goats and pigs
    difference = goats - pigs
    result = difference
    return result

print(solution())