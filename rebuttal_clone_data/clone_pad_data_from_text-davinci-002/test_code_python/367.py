def solution():
     current_salary = 1000000
     employees = 10
     current_employee_salary = 20000
     desired_employee_salary = 35000
     salary_difference = desired_employee_salary - current_employee_salary
     new_salary = current_salary - (salary_difference * employees)
     result = new_salary
     return result

print(solution())