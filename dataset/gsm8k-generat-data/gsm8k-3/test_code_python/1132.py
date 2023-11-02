def solution():
    """In a factory that employed 852 people, 25% more workers have just been hired. How many employees are there now in the factory?"""
    # Define the number of employees originally hired
    original_employees = 852

    # Calculate the 25% increase
    increase_percent = 25
    increase_factor = 1 + (increase_percent/100)

    # Calculate the new number of employees
    new_employees = original_employees * increase_factor

    # Display the new number of employees
    result = new_employees
    return result

print(solution())