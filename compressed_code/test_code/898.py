def solution():
    
    hours_day1 = 10
    hours_day2 = 8
    hours_day3 = 15
    pay_rate = 10
    total_hours = hours_day1 + hours_day2 + hours_day3
    total_pay = total_hours * pay_rate * 2  
    result = total_pay
    return result

print(solution())