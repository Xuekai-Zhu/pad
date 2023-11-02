def solution():
    
    hourly_rate = 30
    hours_worked = 18
    late_penalty = 5
    num_late = 3
    total_penalties = num_late * late_penalty
    total_pay = hourly_rate * hours_worked - total_penalties
    result = total_pay
    return result

print(solution())