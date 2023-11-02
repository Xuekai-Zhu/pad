def solution():
    
    cows = 9
    goats = 4 * cows
    chickens = goats / 2
    total_animals = cows + goats + chickens
    total_chickens = total_animals - (cows + goats)
    result = total_chickens
    return result

print(solution())