def solution():
    """Mrs. Snyder used to spend 40% of her monthly income on rent and utilities. Her salary was recently increased by $600 so now her rent and utilities only amount to 25% of her monthly income. How much was her previous monthly income?"""
    previous_rent_percentage = 40
    current_rent_percentage = 25
    salary_increase = 600
    previous_salary = salary_increase * 100 / (previous_rent_percentage - current_rent_percentage)
    result = previous_salary
    return result

print(solution())