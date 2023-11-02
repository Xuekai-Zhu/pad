def solution():
    total_employees = 480
    salary_increase = 0.1
    travel_allowance_increase = 0.2

    # Calculate the number of employees who got a salary increase
    num_salary_increase = int(total_employees * salary_increase)

    # Calculate the number of employees who got a travel allowance increase
    num_travel_allowance_increase = int(total_employees * travel_allowance_increase)

    # Calculate the total number of employees who got an increase
    num_increase = num_salary_increase + num_travel_allowance_increase

    # Calculate the number of employees who did not get any increase
    num_no_increase = total_employees - num_increase
    result = num_no_increase
    return result

print(solution())