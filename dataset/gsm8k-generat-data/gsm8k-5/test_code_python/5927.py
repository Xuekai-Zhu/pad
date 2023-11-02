def solution():
    num_employees = 9  # There are 9 employees in the office
    time_coffee = 5  # Kim spends 5 minutes making coffee
    time_status_update = 2 * num_employees  # Kim spends 2 minutes per employee for status updates
    time_payroll_update = 3 * num_employees  # Kim spends 3 minutes per employee for payroll updates

    # Calculate the total time for Kim's morning routine
    total_time = time_coffee + time_status_update + time_payroll_update
    result = total_time
    return result

print(solution())