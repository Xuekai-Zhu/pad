def solution():
    required_feet = 300 # Mr. Caiden requires 300 feet of metal roofing
    cost_per_foot = 8 # Each foot of roofing costs $8
    free_feet = 250 # The supplier brings in 250 feet of metal roofing for free

    # Calculate the total cost of the required metal roofing
    total_cost = (required_feet - free_feet) * cost_per_foot
    result = total_cost
    return result

print(solution())