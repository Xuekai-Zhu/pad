def solution():
    cost_per_half_pound = 0.60
    total_budget = 12

    # Calculate the cost per pound of mangoes
    cost_per_pound = cost_per_half_pound * 2

    # Calculate the total number of pounds Kelly can buy
    total_pounds = total_budget / cost_per_pound
    result = total_pounds
    return result

print(solution())