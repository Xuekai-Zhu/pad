def solution():
    years_worked = 6
    current_salary = 10000
    percent_increase = 0.02

    # Calculate the salary increase
    salary_increase = current_salary * percent_increase

    # Calculate the new salary
    new_salary = current_salary + salary_increase

    result = new_salary
    return result

print(solution())