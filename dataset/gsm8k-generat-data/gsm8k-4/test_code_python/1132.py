def solution():
    """In a factory that employed 852 people, 25% more workers have just been hired. How many employees are there now in the factory?"""
    # Define the initial number of employees
    initial_employees = 852

    # Calculate the number of employees with the 25% increase
    new_employees = initial_employees * 0.25

    # Calculate the total number of employees now in the factory
    total_employees = initial_employees + new_employees

    # Return the result
    result = total_employees
    return result

print(solution())