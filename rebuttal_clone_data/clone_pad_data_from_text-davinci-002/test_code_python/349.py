def solution():
     cows = 2
     pigs = 4
     goats = cows - pigs
     total_animals = 56
     num_goats = total_animals - (cows + pigs)
     result = num_goats
     return result

print(solution())