def solution():
    
    total_weight = 1000
    berries_weight = total_weight / 5
    autumn_weight = 2 * berries_weight
    remaining_weight = total_weight - berries_weight - autumn_weight
    small_animals_weight = remaining_weight / 2
    result = small_animals_weight
    return result

print(solution())