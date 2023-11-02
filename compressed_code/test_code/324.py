def solution():
    
    total_gallons = 105
    total_weeks = 3
    daily_gallons_goal = total_gallons / (total_weeks * 7)
    current_daily_gallons = 3
    additional_daily_gallons = daily_gallons_goal - current_daily_gallons
    result = additional_daily_gallons
    return result

print(solution())