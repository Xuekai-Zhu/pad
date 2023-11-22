def solution():
    
    # Define the number of employees and their hourly wage
    num_employees = 40
    hourly_wage = 15

    # Calculate the total wage paid to employees in May
    total_wage = num_employees * hourly_wage * 40

    # Calculate the number of employees who expired in June
    expired_employees = num_employees / 4

    # Calculate the total wage paid to employees in June
    total_wage_expired = expired_employees * hourly_wage * 40

    # Calculate the total pay to employees in the two months
    total_pay = total_wage_expired + total_wage_expired

    # return the result
    result = total_pay
    return result

print(solution())