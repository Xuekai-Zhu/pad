def solution():
    """Bob gets paid $5 an hour for the regular hours he works and $6 an hour for any overtime hours he works. All hours over 40 in a week are considered overtime. If Bob works 44 hours in the first week and 48 hours in the second week, how much did he make?"""
    regular_pay_rate = 5
    overtime_pay_rate = 6
    regular_hours_week1 = 40
    overtime_hours_week1 = 4
    regular_hours_week2 = 40
    overtime_hours_week2 = 8
    
    # Calculate total pay for each week
    week1_pay = (regular_hours_week1 * regular_pay_rate) + (overtime_hours_week1 * overtime_pay_rate)
    week2_pay = (regular_hours_week2 * regular_pay_rate) + (overtime_hours_week2 * overtime_pay_rate)
    
    # Calculate total pay for both weeks
    total_pay = week1_pay + week2_pay
    
    result = total_pay
    return result

print(solution())