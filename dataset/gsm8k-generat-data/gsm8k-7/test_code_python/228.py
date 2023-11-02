def solution():
    total_employees = 200
    drive_to_work_percent = 0.6
    no_drive_percent = 1 - drive_to_work_percent

    # Calculate the number of employees who drive to work
    drive_to_work_employees = total_employees * drive_to_work_percent

    # Calculate the number of employees who don't drive to work
    no_drive_employees = total_employees - drive_to_work_employees

    # Calculate the number of employees who take public transportation
    public_transportation_employees = no_drive_employees / 2

    # Calculate the difference between the number of employees who drive to work and take public transportation
    diff = drive_to_work_employees - public_transportation_employees
    result = diff
    return result

print(solution())