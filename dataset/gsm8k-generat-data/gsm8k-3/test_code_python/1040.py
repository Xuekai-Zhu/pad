def solution():
    """There are 66 goats at a farm and twice as many chickens. If the number of ducks is half of the total of the goats and chickens, and the number of pigs is a third of the number of ducks, how many more goats are there than pigs?"""
    # Determine the number of chickens
    chickens = 66*2

    # Determine the total number of goats and chickens
    goats_and_chickens = 66 + chickens

    # Determine the number of ducks
    ducks = goats_and_chickens/2

    # Determine the number of pigs
    pigs = ducks/3

    # Determine the difference between the number of goats and pigs
    difference = 66 - pigs

    result = difference
    return result

print(solution())