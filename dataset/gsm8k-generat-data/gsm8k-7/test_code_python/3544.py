def solution():
    num_employees = 100
    percent_drive = 0.6
    percent_not_drive = 1 - percent_drive

    # Calculate the number of employees who drive to work
    num_drive = num_employees * percent_drive

    # Calculate the number of employees who don't drive to work
    num_not_drive = num_employees * percent_not_drive

    # Calculate the number of employees who don't drive and take public transportation
    num_public_trans = num_not_drive / 2

    result = num_public_trans
    return result

print(solution())