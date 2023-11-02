def solution():
    """In a grocery store, the daily salary of the manager is $5 and the clerk is $2. If there are currently 2 managers and 3 clerks employed in the grocery store, how much is the total daily salary of all the employees of the grocery store?"""
    manager_salary = 5
    clerk_salary = 2
    num_managers = 2
    num_clerks = 3
    total_salary = (num_managers * manager_salary) + (num_clerks * clerk_salary)
    result = total_salary
    return result

print(solution())