def solution():
    """A company's HR hires 20 new employees every month to add to its total workforce. If the company's initial employee number is 200, and each employee is paid a $4000 salary per month, calculate the total amount of money the company pays to its employees after three months?"""
    initial_employees = 200
    new_employees_per_month = 20
    total_employees_after_three_months = initial_employees + (new_employees_per_month * 3)
    salary_per_employee = 4000
    total_salary_paid_after_three_months = total_employees_after_three_months * salary_per_employee * 3
    result = total_salary_paid_after_three_months
    return result

print(solution())