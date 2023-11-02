def solution():
    # Define the number of employees and the percentages of employees who got each increase
    total_employees = 480
    salary_increase_percentage = 0.1
    travel_allowance_increase_percentage = 0.2

    # Calculate the number of employees who got each increase
    salary_increase_employees = total_employees * salary_increase_percentage
    travel_allowance_increase_employees = total_employees * travel_allowance_increase_percentage

    # Calculate the total number of employees who got an increase
    total_increase_employees = salary_increase_employees + travel_allowance_increase_employees

    # Calculate the number of employees who did not get any increase
    no_increase_employees = total_employees - total_increase_employees
    result = no_increase_employees
    return result

print(solution())