def solution():
    """Emily makes $1,000,000 per year. If she has 10 employees who make $20,000 per year, how much would her salary be if she took part of her salary to make sure all of her employees make $35,000 per year?"""
    emily_salary = 1000000
    num_employees = 10
    current_employee_salary = 20000
    desired_employee_salary = 35000
    total_salary_increase = (desired_employee_salary - current_employee_salary) * num_employees
    new_emily_salary = emily_salary - total_salary_increase
    result = new_emily_salary
    return result

print(solution())