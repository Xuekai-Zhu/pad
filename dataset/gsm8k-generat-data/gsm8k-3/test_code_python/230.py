def solution():
    """A company has 200 employees.  60% of the employees drive to work.  Of the employees who don't drive to work, half take public transportation. How many more employees drive to work than take public transportation?"""
    # Define the number of employees
    total_employees = 200

    # Calculate the number of employees who drive to work
    drive_to_work = int(total_employees * 0.6)

    # Calculate the number of employees who don't drive to work
    no_drive_to_work = total_employees - drive_to_work

    # Calculate the number of employees who take public transportation
    public_transportation = int(no_drive_to_work * 0.5)

    # Calculate the difference between the number of employees who drive to work and those who take public transportation
    difference = drive_to_work - public_transportation

    # Display the difference
    result = difference
    return result

print(solution())