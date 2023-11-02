def solution():
    """A company has 100 employees. 60% of the employees drive to work. Of the employees who don't drive to work, half take public transportation.  How many employees use public transportation to get to work?"""
    # Define the number of employees
    employees = 100

    # Calculate the number of employees who drive to work
    emp_drive = employees * 0.6

    # Calculate the number of employees who don't drive to work
    emp_no_drive = employees - emp_drive

    # Calculate the number of employees who take public transportation
    emp_public_trans = emp_no_drive * 0.5

    # Display the number of employees who use public transportation to get to work
    result = emp_public_trans
    return result

print(solution())