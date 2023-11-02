def solution():
    
    debt = 100
    paid_off = 40
    remaining_debt = debt - paid_off
    hourly_rate = 15
    hours_worked = remaining_debt / hourly_rate
    result = hours_worked
    
    return result

print(solution())