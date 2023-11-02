def solution():
    
    cost_per_week = 36
    cost_per_gallon = 3
    gallons_per_week = cost_per_week / cost_per_gallon
    gallons_per_two_weeks = gallons_per_week * 2
    result = gallons_per_two_weeks
    return result

print(solution())