def solution():
    """A company has 100 employees. 60% of the employees drive to work. Of the employees who don't drive to work, half take public transportation. How many employees use public transportation to get to work?"""
    total_employees = 100
    drive_to_work = total_employees * 0.6
    donot_drive_to_work = total_employees - drive_to_work
    public_transportation = donot_drive_to_work * 0.5
    
    result = public_transportation
    return result

print(solution())