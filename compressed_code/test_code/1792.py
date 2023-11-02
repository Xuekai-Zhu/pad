def solution():
    
    josh_hours_per_month = 8 * 5 * 4
    carl_hours_per_month = (8 - 2) * 5 * 4
    josh_pay_per_hour = 9
    carl_pay_per_hour = 4.5
    josh_total_pay = josh_hours_per_month * josh_pay_per_hour
    carl_total_pay = carl_hours_per_month * carl_pay_per_hour
    total_pay = josh_total_pay + carl_total_pay
    result = total_pay
    return result

print(solution())