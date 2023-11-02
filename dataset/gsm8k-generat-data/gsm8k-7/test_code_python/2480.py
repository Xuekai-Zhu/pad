def solution():
    num_singers = 30
    num_existing_robes = 12
    cost_per_robe = 2

    # Calculate the number of robes the school needs to buy
    num_robes_to_buy = num_singers - num_existing_robes

    # Calculate the total cost of all robes the school needs to buy
    total_cost = num_robes_to_buy * cost_per_robe
    result = total_cost
    return result

print(solution())