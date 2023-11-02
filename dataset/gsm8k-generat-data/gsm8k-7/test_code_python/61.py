def solution():
    weight_needed = 1000
    summer_gain = weight_needed / 5
    autumn_gain = summer_gain * 2
    remaining_weight = weight_needed - summer_gain - autumn_gain
    salmon_gain = remaining_weight / 2
    small_animal_gain = remaining_weight - salmon_gain
    result = small_animal_gain
    return result

print(solution())