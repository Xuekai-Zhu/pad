def solution():
    total_employees = 480
    salary_increase = 0.1 * total_employees
    travel_allowance_increase = 0.2 * total_employees

    # Calculate the number of employees who did not get any increase
    no_increase = total_employees - salary_increase - travel_allowance_increase
    result = no_increase
    return result

print(solution())