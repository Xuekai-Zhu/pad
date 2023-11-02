def solution():
    # Define the weights of the turkeys
    turkey1_weight = 6
    turkey2_weight = 9
    turkey3_weight = turkey2_weight * 2

    # Calculate the total weight of the turkeys
    total_weight = turkey1_weight + turkey2_weight + turkey3_weight

    # Calculate the total cost of the turkeys
    cost_per_kilogram = 2
    total_cost = total_weight * cost_per_kilogram

    result = total_cost
    return result

print(solution())