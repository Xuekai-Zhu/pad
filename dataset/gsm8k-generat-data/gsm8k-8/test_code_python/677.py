def solution():
    # Define the total amount of roofing needed
    total_roofing_needed = 300

    # Define the cost per foot of roofing
    cost_per_foot = 8

    # Calculate the total cost of the roofing needed
    total_cost = total_roofing_needed * cost_per_foot

    # Subtract the amount of free roofing provided by the supplier
    total_cost -= 250 * cost_per_foot

    result = total_cost
    return result

print(solution())