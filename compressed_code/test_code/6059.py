def solution():
    
    emily_salary = 1000000
    num_employees = 10
    current_employee_salary = 20000
    new_employee_salary = 35000
    total_salary_increase = (new_employee_salary - current_employee_salary) * num_employees
    emily_new_salary = emily_salary - total_salary_increase
    result = emily_new_salary
    return result

print(solution())