def solution():
    
    current_salary = 10000
    years_worked = 6
    salary_increase_percent = 2
    new_salary = current_salary * ((100 + salary_increase_percent) / 100)
    result = new_salary
    return result

print(solution())