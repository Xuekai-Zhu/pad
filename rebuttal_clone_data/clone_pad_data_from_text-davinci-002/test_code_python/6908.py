def solution():
    initial_total = 2200
    initial_bodyweight = 245
    percent_increase = 15
    total_increase = initial_total * (percent_increase / 100)
    new_total = initial_total + total_increase
    weight_gain = 8
    new_bodyweight = initial_bodyweight + weight_gain
    total_to_weight_ratio = new_total / new_bodyweight
    result = total_to_weight_ratio
    return result

print(solution())