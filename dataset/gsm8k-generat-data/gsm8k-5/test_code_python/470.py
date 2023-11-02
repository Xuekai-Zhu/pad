def solution():
    normal_wage = 12  # Gary normally earns $12 per hour
    overtime_wage = normal_wage * 1.5  # Gary earns 1.5 times his normal wage for every overtime hour
    total_paycheck = 696  # Gary's paycheck (before taxes are taken out) is $696

    # Calculate the number of hours Gary worked
    if total_paycheck <= 40 * normal_wage:
        hours_worked = total_paycheck / normal_wage
    else:
        overtime_pay = (total_paycheck - (40 * normal_wage)) / 2
        hours_worked = 40 + overtime_pay / overtime_wage

    result = hours_worked
    return result

print(solution())