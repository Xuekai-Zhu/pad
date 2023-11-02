def solution():
    # Calculate the number of employees who drive to work
    drive_to_work = 0.6 * 200 

    # Calculate the number of employees who don't drive to work
    dont_drive_to_work = 200 - drive_to_work 

    # Calculate the number of employees who take public transportation
    take_public_transportation = 0.5 * dont_drive_to_work 

    # Calculate the difference between the number of employees who drive to work and those who take public transportation
    difference = drive_to_work - take_public_transportation
    result = difference
    return result

print(solution())