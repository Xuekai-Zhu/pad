def solution():
    """Queenie earns $150 a day as a part-time clerk. She earns an additional $5 per hour as overtime pay. How much will Queenie receive for working 5 days with 4 hours overtime?"""
    daily_pay = 150
    overtime_pay = 5
    overtime_hours = 4
    days_worked = 5

    regular_pay = daily_pay * days_worked
    overtime_pay_per_day = overtime_hours * overtime_pay
    overtime_pay_total = overtime_pay_per_day * days_worked

    total_pay = regular_pay + overtime_pay_total
    result = total_pay
    
    return result

print(solution())