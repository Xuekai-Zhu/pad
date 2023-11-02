def solution():
     apple_seeds = 6
     pear_seeds = 2
     grape_seeds = 3
     apples = 4
     pears = 3
     grapes = 9
     seeds_from_apples = apple_seeds * apples
     seeds_from_pears = pear_seeds * pears
     seeds_from_grapes = grape_seeds * grapes
     total_seeds = seeds_from_apples + seeds_from_pears + seeds_from_grapes
     result = 60 - total_seeds
     return result

print(solution())