def solution():
    
    num_reps = 50
    hours_per_day = 8
    hourly_rate = 14
    days_worked = 5
    total_hours = num_reps * hours_per_day * days_worked
    total_pay = total_hours * hourly_rate
    result = total_pay
    return result

print(solution())