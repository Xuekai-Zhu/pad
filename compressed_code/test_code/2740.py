def solution():
    
    days_per_week = 5
    hours_per_day = 4
    wage_per_hour = 5
    total_hours = days_per_week * hours_per_day
    weekly_earning = total_hours * wage_per_hour
    school_allocation = 0.75 * weekly_earning
    result = school_allocation
    return result

print(solution())