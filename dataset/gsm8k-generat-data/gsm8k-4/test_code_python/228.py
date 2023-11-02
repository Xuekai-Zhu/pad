def solution():
    """A company has 200 employees.  60% of the employees drive to work.  Of the employees who don't drive to work, half take public transportation. How many more employees drive to work than take public transportation?"""
    # Define the total number of employees and the percentage that drive to work
    total_employees = 200
    drive_percentage = 0.6

    # Calculate the number of employees that drive to work
    drive_employees = total_employees * drive_percentage

    # Calculate the number of employees that don't drive to work
    nodrive_employees = total_employees - drive_employees

    # Calculate the number of employees that take public transportation
    public_trans_employees = nodrive_employees * 0.5

    # Calculate the difference between the number of employees that drive and take public transportation
    diff = drive_employees - public_trans_employees

    # Return the result
    result = diff
    return result

print(solution())