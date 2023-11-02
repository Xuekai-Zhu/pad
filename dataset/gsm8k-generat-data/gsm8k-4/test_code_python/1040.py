def solution():
    """There are 66 goats at a farm and twice as many chickens. If the number of ducks is half of the total of the goats and chickens, and the number of pigs is a third of the number of ducks, how many more goats are there than pigs?"""
    # Define the number of goats and calculate the number of chickens
    goats = 66
    chickens = goats * 2

    # Calculate the number of ducks
    ducks = (goats + chickens) / 2

    # Calculate the number of pigs
    pigs = ducks / 3

    # Calculate the difference in the number of goats and pigs
    goat_pig_difference = goats - pigs

    result = goat_pig_difference
    return result

print(solution())