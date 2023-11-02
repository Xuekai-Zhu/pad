def solution():
     cows = 4
     sheep = 3
     chickens = 7
     bushels_per_cow = 2
     bushels_per_sheep = 2
     bushels_per_chicken = 3
     total_bushels = (cows * bushels_per_cow) + (sheep * bushels_per_sheep) + (chickens * bushels_per_chicken)
     result = total_bushels
     return result

print(solution())