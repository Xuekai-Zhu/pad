def solution():
    
    hourly_rate = 250
    hours_per_day = 6
    days_per_week = 4
    weeks_per_5 = 5
    total_hours_worked = hours_per_day * days_per_week * weeks_per_5
    total_pay = total_hours_worked * hourly_rate
    discount = total_pay * 0.1
    final_pay = total_pay - discount
    result = final_pay
    return result

print(solution())