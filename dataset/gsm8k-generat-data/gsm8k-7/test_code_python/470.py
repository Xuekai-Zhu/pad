def solution():
    normal_wage = 12
    overtime_multiplier = 1.5
    overtime_threshold = 40
    total_paycheck = 696

    # Calculate the number of hours worked before overtime
    normal_hours = total_paycheck // normal_wage

    # Calculate the amount of overtime pay earned
    overtime_pay = (total_paycheck - (normal_hours * normal_wage)) / overtime_multiplier

    # Calculate the number of overtime hours worked
    overtime_hours = overtime_pay / normal_wage

    # Calculate the total number of hours worked
    total_hours = normal_hours + overtime_hours

    result = total_hours
    return result

print(solution())