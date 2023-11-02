def solution():
    """Mrs. Snyder used to spend 40% of her monthly income on rent and utilities. Her salary was recently increased by $600 so now her rent and utilities only amount to 25% of her monthly income. How much was her previous monthly income?"""
    current_rent_percent = 0.25
    previous_rent_percent = 0.4
    salary_increase = 600
    previous_salary = (salary_increase / (current_rent_percent - previous_rent_percent)) + salary_increase
    result = previous_salary
    return result

print(solution())