def solution():
    """Kim is an office manager. Every morning she spends 5 minutes making coffee, 2 minutes per employee getting a status update, and 3 minutes per employee updating payroll records. If there are 9 employees in the office, how long does Kim's morning routine take?"""
    # Define the time it takes to make coffee
    coffee_time = 5

    # Define the time it takes to get a status update from each employee and update their payroll records
    per_employee_time = 2 + 3

    # Calculate the total time it takes to get a status update from and update payroll records for all employees
    employees = 9
    total_employee_time = per_employee_time * employees

    # Calculate the total time of Kim's morning routine
    total_time = coffee_time + total_employee_time

    # Display the result
    result = total_time
    return result

print(solution())