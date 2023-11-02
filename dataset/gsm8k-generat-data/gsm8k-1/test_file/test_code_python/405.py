def solution():
    """Carolyn works for a delivery service company that hires on a contract basis. 
    In May, they hired 40 employees, paying each employee $15 per hour for a 40-hour workweek. 
    In June, 1/4 of the employees' contracts expired. Calculate the total amount of money the company paid to the employees in the two months."""
    may_employees = 40
    june_employees = may_employees - (may_employees // 4)
    hourly_rate = 15
    work_hours = 40
    may_pay = may_employees * hourly_rate * work_hours
    june_pay = june_employees * hourly_rate * work_hours
    total_pay = may_pay + june_pay
    result = total_pay
    return result

print(solution())