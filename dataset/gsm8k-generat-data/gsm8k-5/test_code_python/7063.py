def solution():
    # Calculate the total bonus amount
    total_bonus = 0.25 * 5000000

    # Calculate the number of female employees who are mothers
    num_female_mothers = (2/3) * 3300 - 1200

    # Calculate the bonus amount per female mother employee
    bonus_per_employee = total_bonus / num_female_mothers
    result = bonus_per_employee
    return result

print(solution())