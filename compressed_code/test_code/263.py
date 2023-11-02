def solution():
    
    emily_salary = 1000000
    num_employees = 10
    current_employee_salary = 20000
    desired_employee_salary = 35000
    total_salary_increase = (desired_employee_salary - current_employee_salary) * num_employees
    new_emily_salary = emily_salary - total_salary_increase
    result = new_emily_salary
    return result

print(solution())