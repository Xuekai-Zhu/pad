def solution():
    """Kim is an office manager. Every morning she spends 5 minutes making coffee, 2 minutes per employee getting a status update, and 3 minutes per employee updating payroll records. If there are 9 employees in the office, how long does Kim's morning routine take?"""
    # Define the time Kim spends on each task
    COFFEE_TIME = 5
    STATUS_UPDATE_TIME = 2
    PAYROLL_UPDATE_TIME = 3

    # Define the number of employees in the office
    n_employees = 9

    # Calculate the total time Kim spends on getting status updates and updating payroll records
    employee_time = (STATUS_UPDATE_TIME + PAYROLL_UPDATE_TIME) * n_employees

    # Calculate the total time Kim's morning routine takes
    total_time = COFFEE_TIME + employee_time

    # Display the total time
    result = total_time
    return result

print(solution())