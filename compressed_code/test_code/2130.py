def solution():
    
    regular_pay_rate = 5
    overtime_pay_rate = 6
    first_week_hours = 44
    second_week_hours = 48
    if first_week_hours <= 40:
        first_week_pay = first_week_hours * regular_pay_rate
    else:
        first_week_pay = 40 * regular_pay_rate + (first_week_hours - 40) * overtime_pay_rate
    if second_week_hours <= 40:
        second_week_pay = second_week_hours * regular_pay_rate
    else:
        second_week_pay = 40 * regular_pay_rate + (second_week_hours - 40) * overtime_pay_rate
    total_pay = first_week_pay + second_week_pay
    result = total_pay
    return result

print(solution())