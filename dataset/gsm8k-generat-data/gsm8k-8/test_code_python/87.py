def solution():
    starting_weight = 400
    final_weight = 1.5 * starting_weight
    price_per_pound = 3

    starting_value = starting_weight * price_per_pound
    final_value = final_weight * price_per_pound

    increase_in_value = final_value - starting_value
    result = increase_in_value
    return result

print(solution())