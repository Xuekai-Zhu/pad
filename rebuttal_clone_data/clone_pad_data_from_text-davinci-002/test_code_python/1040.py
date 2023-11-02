def solution():
     goats = 66
     chickens = goats * 2
     ducks = (goats + chickens) / 2
     pigs = ducks / 3
     goats_minus_pigs = goats - pigs
     result = goats_minus_pigs
     return result

print(solution())