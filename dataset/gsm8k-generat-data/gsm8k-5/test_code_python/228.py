def solution():
    total_employees = 200  # The company has 200 employees
    drive_to_work = total_employees * 0.6  # 60% of the employees drive to work
    dont_drive = total_employees - drive_to_work  # The remaining employees don't drive to work
    take_public_trans = dont_drive / 2  # Half of the employees who don't drive take public transportation

    # Calculate the difference between the number of employees who drive to work and those who take public transportation
    diff = drive_to_work - take_public_trans
    result = diff
    return result

print(solution())