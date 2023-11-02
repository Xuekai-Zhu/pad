def solution():
    """There are 66 goats at a farm and twice as many chickens. If the number of ducks is half of the total of the goats and chickens, and the number of pigs is a third of the number of ducks, how many more goats are there than pigs?"""
    goats = 66
    chickens = goats * 2
    ducks = (goats + chickens) / 2
    pigs = ducks / 3
    goat_difference = goats - pigs
    result = goat_difference
    return result

print(solution())