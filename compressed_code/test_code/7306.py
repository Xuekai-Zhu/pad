def solution():
    
    current_salary = 10000
    years_worked = 6
    salary_increase_percent = 2
    salary_increase = current_salary * (salary_increase_percent / 100)
    new_salary = current_salary + salary_increase
    result = new_salary
    return result

print(solution())