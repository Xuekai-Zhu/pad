def solution():
    # Calculate the weight of the third turkey
    weight_third_turkey = 2 * 9  # Twice the weight of the second turkey

    # Calculate the total weight of the turkeys
    total_weight = 6 + 9 + weight_third_turkey

    # Calculate the total cost of the turkeys
    cost_per_kilogram = 2  # $2 per kilogram of turkey
    total_cost = total_weight * cost_per_kilogram
    result = total_cost
    return result

print(solution())