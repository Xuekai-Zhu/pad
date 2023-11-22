def solution():
    
    regular_rate = 20
    regular_hours = 8
    extra_hours = 10
    extra_rate = regular_rate * 1.5
    total_hours = regular_hours + extra_hours + 11
    total_pay = total_hours * regular_rate + extra_hours * extra_rate
    result = total_pay
    return result

print(solution())