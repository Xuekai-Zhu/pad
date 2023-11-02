def solution():
    manager_salary = 5
    clerk_salary = 2
    num_managers = 2
    num_clerks = 3

    # Calculate the total daily salary for all managers
    total_manager_salary = manager_salary * num_managers

    # Calculate the total daily salary for all clerks
    total_clerk_salary = clerk_salary * num_clerks

    # Calculate the total daily salary for all employees
    total_salary = total_manager_salary + total_clerk_salary
    result = total_salary
    return result

print(solution())