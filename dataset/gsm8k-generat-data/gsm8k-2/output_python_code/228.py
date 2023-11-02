def solution():
    """A company has 200 employees. 60% of the employees drive to work. Of the employees who don't drive to work, half take public transportation. How many more employees drive to work than take public transportation?"""
    total_employees = 200
    drive_to_work_percent = 0.6
    drive_to_work = total_employees * drive_to_work_percent
    dont_drive_to_work = total_employees - drive_to_work
    public_transportation = dont_drive_to_work / 2
    difference = drive_to_work - public_transportation
    result = difference
    return result

print(solution())