def solution():
    """Out of 480 employees, 10% got a salary increase while 20% got a travel allowance increase. How many employees did not get any increase?"""
    total_employees = 480
    salary_increase = 0.1 * total_employees
    travel_allowance_increase = 0.2 * total_employees
    no_increase = total_employees - salary_increase - travel_allowance_increase
    result = no_increase
    return result

print(solution())