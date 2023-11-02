def solution():
    weight_needed = 1000
    berries_gain = weight_needed / 5
    acorns_gain = 2 * berries_gain
    remaining_weight_needed = weight_needed - berries_gain - acorns_gain
    salmon_gain = remaining_weight_needed / 2
    small_animals_gain = remaining_weight_needed - salmon_gain
    result = small_animals_gain
    return result

print(solution())