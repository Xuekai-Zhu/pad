def solution():
    
    base_pay_per_day = 80
    bonus_pay_per_day = 20
    extra_hours_worked = 2
    total_hours_worked = 8 + extra_hours_worked
    total_pay_per_day = base_pay_per_day + bonus_pay_per_day
    total_pay_per_hour = total_pay_per_day / total_hours_worked
    result = total_pay_per_hour
    
    return result

print(solution())