def solution():
    
    hours_per_day = 7.5
    days_per_week = 6
    hourly_rate = 1.5
    extra_money = 10
    weeks_in_april = 4
    total_hours = hours_per_day * days_per_week * weeks_in_april
    total_money = total_hours * hourly_rate + extra_money
    result = total_money
    return result

print(solution())