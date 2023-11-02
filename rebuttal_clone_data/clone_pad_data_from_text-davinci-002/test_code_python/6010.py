def solution():
    total_weight = 300
    increase_percentage = 30
    increase_amount = total_weight * (increase_percentage / 100)
    total_weight_straps = total_weight + increase_amount
    new_distance = 20 + (10 * 0.5)
    new_distance_percentage = (new_distance / 20)
    new_weight = total_weight_straps * new_distance_percentage
    result = new_weight
    return result

print(solution())