def solution():
    """In a grocery store, the daily salary of the manager is $5 and the clerk is $2. If there are currently 2 managers and 3 clerks employed in the grocery store, how much is the total daily salary of all the employees of the grocery store?"""
    # Define the daily salary of each employee
    MANAGER_SALARY = 5
    CLERK_SALARY = 2

    # Define the number of managers and clerks employed
    num_managers = 2
    num_clerks = 3

    # Calculate the total daily salary
    total_salary = (num_managers * MANAGER_SALARY) + (num_clerks * CLERK_SALARY)

    # Display the total daily salary
    result = total_salary
    return result

print(solution())