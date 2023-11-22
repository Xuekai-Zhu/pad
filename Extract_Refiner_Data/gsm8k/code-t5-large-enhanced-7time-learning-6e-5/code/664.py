def solution():
    
    # Define the total number of employees
    total_employees = 50

    # Calculate the number of employees who are management
    management_employees = total_employees * 0.2

    # Calculate the number of employees who are overseeing the entire company
    overseeing_employees = total_employees * 0.3

    # Display the number of employees who oversee the company
    result = overseeing_employees
    return result

print(solution())