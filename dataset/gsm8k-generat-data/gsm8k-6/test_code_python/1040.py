def solution():
    goats = 66
    chickens = goats * 2
    ducks = (goats + chickens) / 2
    pigs = ducks / 3
    diff = goats - pigs

    result = diff
    return result

print(solution())