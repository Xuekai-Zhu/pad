def solution():
    # Define the cost of cheddar cheese and cream cheese
    cheddar_cost = 10
    cream_cost = 0.5 * cheddar_cost

    # Define the cost of the cold cuts
    cold_cuts_cost = 2 * cheddar_cost

    # Calculate the total cost of the ingredients
    total_cost = cheddar_cost + cream_cost + cold_cuts_cost
    result = total_cost
    return result

print(solution())