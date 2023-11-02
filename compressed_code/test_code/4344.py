def solution():
    
    hours_per_week = 40
    hourly_wage = 11.50
    total_hours = hours_per_week * 2
    gross_pay = total_hours * hourly_wage
    remaining_money = gross_pay - 410
    result = remaining_money
    return result

print(solution())