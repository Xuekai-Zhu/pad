def solution():
    starting_weight = 400
    weight_increase = 1.5
    selling_price_per_pound = 3

    # Calculate the new weight of the cow
    new_weight = starting_weight * weight_increase

    # Calculate the difference in value before and after the weight gain
    value_increase = (new_weight - starting_weight) * selling_price_per_pound

    result = value_increase
    return result

print(solution())