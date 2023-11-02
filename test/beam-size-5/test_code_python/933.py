def solution():
    
    goats = 15
    sheep = 12
    goat_weight = 5
    sheep_weight = 2 * goat_weight - 3
    total_goat_weight = goats * goat_weight
    total_sheep_weight = sheep * sheep_weight
    total_hay_weight = total_goat_weight + total_sheep_weight
    result = total_hay_weight
    return result

print(solution())