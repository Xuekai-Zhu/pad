def solution():
    coffee_time = 5
    status_update_time = 2
    payroll_time = 3
    num_employees = 9

    # Calculate the total time Kim spends on status updates and payroll
    employee_time = (status_update_time + payroll_time) * num_employees

    # Calculate the total time for Kim's morning routine
    total_time = coffee_time + employee_time
    result = total_time
    return result

print(solution())