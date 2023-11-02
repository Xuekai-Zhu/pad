def solution():
    # Calculate the total number of hours worked per week by one employee
    weekly_hours = 10 * 5
    
    # Calculate the total number of hours worked per month by one employee
    monthly_hours = weekly_hours * 4
    
    # Calculate the monthly salary of one employee
    employee_salary = 12 * monthly_hours
    
    # Calculate the total salary paid to 500 employees per month
    total_monthly_salary = 500 * employee_salary
    
    # Calculate the total monthly salary after the new hires
    new_total_employee = 500 + 200
    new_employee_salary = 12 * monthly_hours
    new_total_monthly_salary = new_total_employee * new_employee_salary
    
    result = new_total_monthly_salary
    return result

print(solution())