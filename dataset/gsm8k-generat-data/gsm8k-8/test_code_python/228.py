def solution():
    # Calculate the number of employees who drive to work
    drive_to_work = 0.6 * 200

    # Calculate the number of employees who don't drive to work
    no_drive_to_work = 200 - drive_to_work

    # Calculate the number of employees who take public transportation
    public_transportation = 0.5 * no_drive_to_work

    # Calculate the difference between the number of employees who drive and take public transportation
    diff = drive_to_work - public_transportation

    result = diff
    return result

print(solution())