def solution():
    total_feet = 300  # total feet of metal roofing required
    cost_per_foot = 8  # cost of each foot of roofing
    free_feet = 250  # feet of metal roofing brought in for free

    # Calculate the total cost of the metal roofing required
    total_cost = (total_feet - free_feet) * cost_per_foot
    result = total_cost
    return result

print(solution())