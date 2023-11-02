def solution():
    # Calculate the number of employees who drive to work
    drive_to_work = 0.6 * 100

    # Calculate the number of employees who don't drive to work
    dont_drive_to_work = 100 - drive_to_work

    # Calculate the number of employees who take public transportation
    take_public_transportation = 0.5 * dont_drive_to_work

    result = take_public_transportation
    return result

print(solution())