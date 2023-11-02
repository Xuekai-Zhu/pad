def solution():
    total_weight = 30
    weight_in_ounces = total_weight * 16
    food_per_half_pound = 1
    food_needed = weight_in_ounces / 2 * food_per_half_pound
    jars_needed = food_needed / 15
    cost = jars_needed * 2
    result = cost
    return result

print(solution())