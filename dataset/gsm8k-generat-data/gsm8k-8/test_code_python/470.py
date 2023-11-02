def solution():
    # Define the normal hourly wage and the overtime multiplier
    normal_wage = 12
    overtime_multiplier = 1.5

    # Define the total amount earned before taxes
    total_earned = 696

    # Calculate the number of regular hours worked
    regular_hours = 40
    regular_pay = normal_wage * regular_hours

    # Calculate the amount earned from overtime
    overtime_pay = total_earned - regular_pay
    overtime_hours = overtime_pay / (normal_wage * overtime_multiplier)

    # Calculate the total number of hours worked
    total_hours = regular_hours + overtime_hours
    result = total_hours
    return result

print(solution())