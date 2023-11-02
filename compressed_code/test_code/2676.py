def solution():
    
    hourly_pay = 30
    weekly_hours = 18
    late_penalties = 5 * 3
    total_pay = (hourly_pay * weekly_hours) - late_penalties
    result = total_pay
    return result

print(solution())