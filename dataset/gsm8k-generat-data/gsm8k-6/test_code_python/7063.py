def solution():
    # Calculate the number of female mother employees
    female_employees = 3300 * (2/3)  # one-third of the employees are men, so two-thirds are women
    female_mothers = female_employees - 1200  # 1200 of the female employees are not mothers
    # Calculate the total bonus amount for all female mother employees
    total_bonus = 0.25 * 5000000  # 25% of Facebook's annual earnings for 2020
    # Calculate the bonus amount for each female mother employee
    bonus_per_employee = total_bonus / female_mothers
    result = bonus_per_employee
    return result

print(solution())