def solution():
    # Calculate the number of female employees who are mothers
    num_female_mothers = (2 / 3) * 3300 - 1200

    # Calculate the total bonus amount for female mother employees
    bonus_total = 0.25 * 5000000

    # Calculate the amount of bonus each female mother employee received
    bonus_per_employee = bonus_total / num_female_mothers

    result = bonus_per_employee
    return result

print(solution())