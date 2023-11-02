def solution():
    # Define the initial salary and years worked
    initial_salary = 10000
    years_worked = 6

    # Calculate the salary increase
    salary_increase = initial_salary * (2/100)

    # Calculate the new salary
    new_salary = initial_salary + salary_increase

    result = new_salary
    return result

print(solution())