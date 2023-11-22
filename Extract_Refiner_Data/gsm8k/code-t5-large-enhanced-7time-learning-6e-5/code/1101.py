def solution():
    
    current_salary = 100000
    savings_percentage = 0.2
    years_to_save = 20
    annual_salary = current_salary * (1 - annual_salary_percentage)
    years_to_save_needed = annual_salary / savings_percentage
    result = years_to_save_needed
    return result

print(solution())