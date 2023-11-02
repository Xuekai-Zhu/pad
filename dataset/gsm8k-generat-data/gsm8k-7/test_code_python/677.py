def solution():
    required_feet = 300
    cost_per_foot = 8
    free_feet = 250

    # Calculate the total cost of all the required metal roofing
    total_cost = (required_feet - free_feet) * cost_per_foot
    result = total_cost
    return result

print(solution())