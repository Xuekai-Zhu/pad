def solution():
    
    regular_pay_rate = 5
    overtime_pay_rate = 6
    regular_hours_week1 = 40
    overtime_hours_week1 = 4
    regular_hours_week2 = 40
    overtime_hours_week2 = 8
    
    
    week1_pay = (regular_hours_week1 * regular_pay_rate) + (overtime_hours_week1 * overtime_pay_rate)
    week2_pay = (regular_hours_week2 * regular_pay_rate) + (overtime_hours_week2 * overtime_pay_rate)
    
    
    total_pay = week1_pay + week2_pay
    
    result = total_pay
    return result

print(solution())