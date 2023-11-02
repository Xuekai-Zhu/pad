def solution():
    
    total_weight_needed = 1000
    berries_weight = total_weight_needed / 5
    autumn_weight = (total_weight_needed - berries_weight) / 2
    salmon_weight = (total_weight_needed - berries_weight - autumn_weight) / 2
    small_animal_weight = total_weight_needed - berries_weight - autumn_weight - salmon_weight
    result = small_animal_weight
    return result

print(solution())