def solution():
    
    last_week_hours = 35
    last_week_pay = last_week_hours * 10
    new_hourly_rate = 10.5
    this_week_hours = 40
    this_week_pay = this_week_hours * new_hourly_rate
    total_pay = last_week_pay + this_week_pay
    result = total_pay
    return result

print(solution())