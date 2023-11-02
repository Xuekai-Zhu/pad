def solution():
    """Kim is an office manager. Every morning she spends 5 minutes making coffee, 2 minutes per employee getting a status update, and 3 minutes per employee updating payroll records. If there are 9 employees in the office, how long does Kim's morning routine take?"""
    num_employees = 9
    coffee_time = 5
    status_time = 2 * num_employees
    payroll_time = 3 * num_employees
    total_time = coffee_time + status_time + payroll_time
    result = total_time
    return result

print(solution())