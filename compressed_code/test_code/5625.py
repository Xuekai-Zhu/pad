def solution():
    
    cows = 20
    foxes = 15
    zebras = 3 * foxes
    total_animals = cows + foxes + zebras
    sheep = 100 - total_animals
    result = sheep
    return result

print(solution())