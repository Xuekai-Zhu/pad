def solution():
    
    work_days = 15  
    hours_per_day = 12
    hourly_rate = 20
    raise_percent = 0.3
    new_rate = hourly_rate * (1 + raise_percent)
    total_pay = work_days * hours_per_day * new_rate
    result = total_pay
    return result

print(solution())