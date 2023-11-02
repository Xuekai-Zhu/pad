def solution():
    """A company has 200 employees. 60% of the employees drive to work. Of the employees who don't drive to work, half take public transportation. How many more employees drive to work than take public transportation?"""
    total_employees = 200
    drive_percent = 60
    drive_count = (drive_percent / 100) * total_employees
    no_drive_count = total_employees - drive_count
    public_transport_count = no_drive_count / 2
    difference = drive_count - public_transport_count
    result = difference
    return result

print(solution())