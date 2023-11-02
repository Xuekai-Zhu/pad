def solution():
    # Calculate the total amount of money made by Emily's employees
    employee_income = 10 * 20000  # 10 employees making $20,000 per year

    # Calculate how much Emily would need to contribute to ensure her employees make $35,000 per year
    difference = 35000 - 20000  # the difference between their current salary and the targeted salary
    total_contribution = difference * 10  # the total contribution needed to achieve the targeted salary for all employees

    # Calculate Emily's new salary after making the necessary contribution
    new_salary = 1000000 - total_contribution

    result = new_salary
    return result

print(solution())