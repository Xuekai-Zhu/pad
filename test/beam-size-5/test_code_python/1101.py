def solution():
    
    current_salary = 100000
    annual_salary = current_salary * 0.4
    years_to_save = (current_salary - annual_salary) / 0.2
    result = years_to_save
    return result

print(solution())