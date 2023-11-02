def solution():
    hours_per_week = 40  # Both employees work for 40 hours per week

    # Calculate the weekly salary for the first employee
    salary_employee_1 = 20 * hours_per_week

    # Calculate the weekly salary for the second employee
    salary_employee_2 = (22 - 6) * hours_per_week  # $6 subsidy from the government for hiring a disabled worker

    # Calculate the difference in weekly salaries
    savings = salary_employee_1 - salary_employee_2
    result = savings
    return result

print(solution())