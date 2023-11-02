def solution():
    
    hourly_rate = 15
    hours_worked = 3
    total_pay = hourly_rate * hours_worked
    tip = 0.2 * total_pay
    total_cost = total_pay + tip
    result = total_cost
    return result

print(solution())