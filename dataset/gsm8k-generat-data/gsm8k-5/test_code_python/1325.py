def solution():
    salary_last_month = 1000  # Sally earned $1000 last month
    raise_percentage = 10  # Sally received a 10% raise this month

    # Calculate Sally's salary this month
    salary_this_month = salary_last_month * (1 + raise_percentage / 100)

    # Calculate Sally's total salary for the two months
    total_salary = salary_last_month + salary_this_month
    result = total_salary
    return result

print(solution())