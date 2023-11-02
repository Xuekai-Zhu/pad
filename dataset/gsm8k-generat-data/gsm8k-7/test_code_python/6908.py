def solution():
    original_total = 2200
    original_weight = 245
    weight_gain = 8
    total_gain = original_total * 0.15
    new_total = original_total + total_gain
    new_weight = original_weight + weight_gain
    ratio = new_total / new_weight
    result = round(ratio, 2) # round to 2 decimal places
    return result

print(solution())