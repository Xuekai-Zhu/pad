def solution():
    """Sally earned $1000 at work last month. This month, she received a 10% raise. How much money will she make in total for the two months?"""
    salary_last_month = 1000
    raise_percentage = 0.1
    salary_this_month = salary_last_month * (1 + raise_percentage)
    total_salary = salary_last_month + salary_this_month
    result = total_salary
    return result

print(solution())