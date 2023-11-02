def solution():
    
    goats = 66
    chickens = goats * 2
    ducks = (goats + chickens) / 2
    pigs = ducks / 3
    goat_difference = goats - pigs
    result = goat_difference
    return result

print(solution())