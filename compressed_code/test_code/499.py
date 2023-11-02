def solution():
    
    needed_feet = 300
    cost_per_foot = 8
    free_feet = 250
    remaining_feet = needed_feet - free_feet
    total_cost = remaining_feet * cost_per_foot
    result = total_cost
    return result

print(solution())