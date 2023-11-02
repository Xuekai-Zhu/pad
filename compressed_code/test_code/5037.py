def solution():
    
    hourly_rate = 20
    monthly_expenses = 1200
    weekday_hours = 3 * 5
    saturday_hours = 5
    total_hours_per_week = weekday_hours + saturday_hours
    total_earned_per_week = total_hours_per_week * hourly_rate
    weeks_to_cover_expenses = monthly_expenses / total_earned_per_week
    result = weeks_to_cover_expenses
    return result

print(solution())