def solution():
    
    goats = 66
    chickens = 2 * goats
    ducks = (goats + chickens) / 2
    pigs = ducks / 3
    difference = goats - pigs
    result = difference
    return result

print(solution())