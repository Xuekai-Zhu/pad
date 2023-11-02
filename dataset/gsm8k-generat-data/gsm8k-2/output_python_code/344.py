def solution():
    """Adam earns $40 daily in his job. 10% of his money is deducted as taxes. How much money will Adam have earned after taxes after 30 days of work?"""
    daily_salary = 40
    tax_percentage = 0.1
    salary_after_tax = daily_salary * (1 - tax_percentage)
    total_salary = salary_after_tax * 30
    result = total_salary
    return result

print(solution())