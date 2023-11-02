def solution():
    """Lucille has to divide the revenue from her business in the ratio of 4:11 for employee salaries and stock purchases, respectively. If she has $3000 as her revenue, calculate the total amount of money she spends on employee salary?"""
    total_ratio = 4 + 11 
    employee_salary_ratio = 4
    revenue = 3000
    
    employee_salary = (employee_salary_ratio/total_ratio) * revenue
    result = employee_salary
    
    return result

print(solution())