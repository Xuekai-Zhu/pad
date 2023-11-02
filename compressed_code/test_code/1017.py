def solution():
    
    salary_last_month = 1000
    raise_percentage = 0.1
    salary_this_month = salary_last_month * (1 + raise_percentage)
    total_salary = salary_last_month + salary_this_month
    result = total_salary
    return result

print(solution())