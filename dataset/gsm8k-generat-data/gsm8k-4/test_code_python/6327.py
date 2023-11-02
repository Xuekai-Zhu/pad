def solution():
    """Out of 480 employees, 10% got a salary increase while 20% got a travel allowance increase. How many employees did not get any increase?"""
    # Define the total number of employees
    total_employees = 480

    # Calculate the number of employees who got a salary increase
    salary_increase_employees = total_employees * 0.1

    # Calculate the number of employees who got a travel allowance increase
    travel_increase_employees = total_employees * 0.2

    # Calculate the number of employees who did not get any increase
    no_increase_employees = total_employees - salary_increase_employees - travel_increase_employees

    # return the result
    result = no_increase_employees
    return result

print(solution())