def solution():
    turkey1_weight = 6 #in kilograms
    turkey2_weight = 9 #in kilograms
    turkey3_weight = turkey2_weight * 2 #in kilograms

    cost_per_kilogram = 2 #in dollars

    # Calculate the total cost of turkey1
    turkey1_cost = turkey1_weight * cost_per_kilogram

    # Calculate the total cost of turkey2
    turkey2_cost = turkey2_weight * cost_per_kilogram

    # Calculate the total cost of turkey3
    turkey3_cost = turkey3_weight * cost_per_kilogram

    # Calculate the total cost of all turkeys
    total_cost = turkey1_cost + turkey2_cost + turkey3_cost
    result = total_cost
    return result

print(solution())