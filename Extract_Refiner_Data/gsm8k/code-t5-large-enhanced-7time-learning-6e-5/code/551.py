def solution():
    
    hourly_rate = 2
    hours_per_day = 5
    days_per_week = 4
    total_hours_per_week = hours_per_day * days_per_week
    total_pay_per_week = total_hours_per_week * hourly_rate
    weeks_to_save = 80 / total_pay_per_week
    result = weeks_to_save
    return result

print(solution())