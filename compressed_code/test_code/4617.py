def solution():
    
    growth_per_week = 2
    initial_height = 10
    weeks_in_4_months = 4 * 4
    total_growth = growth_per_week * weeks_in_4_months
    total_height = initial_height + total_growth
    result = total_height
    return result

print(solution())