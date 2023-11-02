def solution():
    """Lucille has to divide the revenue from her business in the ratio 4:11 for employee salaries and stock purchases, respectively. If she has $3000 as her revenue, calculate the total amount of money she spends on employee salary?"""
    total_ratio = 4 + 11
    employee_salary_ratio = 4 / total_ratio
    total_revenue = 3000
    employee_salary_amount = employee_salary_ratio * total_revenue
    result = employee_salary_amount
    return result

print(solution())