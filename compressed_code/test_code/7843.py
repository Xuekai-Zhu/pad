def solution():
    
    cows = 12
    sheep = cows * 2
    pigs_per_sheep = 3
    pigs = sheep * pigs_per_sheep
    total_animals = cows + sheep + pigs
    result = total_animals
    return result

print(solution())