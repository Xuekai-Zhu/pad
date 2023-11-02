def solution():
    hours_per_day = 8
    hourly_rate = 16
    extra_hours = 2
    extra_hourly_rate = 13.50
    days_per_week = 5
    total_hours = hours_per_day + (extra_hours * days_per_week)
    total_wage = total_hours * hourly_rate + (extra_hourly_rate * extra_hours * days_per_week)
    
    return total_wage

print(solution())