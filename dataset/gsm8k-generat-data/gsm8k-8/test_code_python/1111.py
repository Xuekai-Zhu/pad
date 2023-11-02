def solution():
    # Calculate the cost of the steaks
    steak_weight = 4.5
    steak_cost_per_pound = 15
    steak_cost = steak_weight * steak_cost_per_pound

    # Calculate the cost of the chicken breasts
    chicken_weight = 1.5
    chicken_cost_per_pound = 8
    chicken_cost = chicken_weight * chicken_cost_per_pound

    # Calculate the total cost
    total_cost = steak_cost + chicken_cost
    result = total_cost
    return result

print(solution())