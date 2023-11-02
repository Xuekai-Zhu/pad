def solution():
    
    starting_height = 66
    growth_per_month = 2
    num_months = 3
    final_height_inches = starting_height + (growth_per_month * num_months)
    final_height_feet = final_height_inches / 12
    result = final_height_feet
    return result

print(solution())