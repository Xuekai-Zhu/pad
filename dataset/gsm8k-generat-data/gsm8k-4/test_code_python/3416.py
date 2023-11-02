def solution():
    """September's temperature fluctuated severely in 1 week. They started off with 40 degrees on Sunday then hit 50 on Monday, 65 on Tuesday, 36 on Wednesday, 82 on Thursday, 72 on Friday and ended the week at 26 on Saturday. What was the average temperature for that week?"""
    # Define the temperatures for each day of the week
    sunday = 40
    monday = 50
    tuesday = 65
    wednesday = 36
    thursday = 82
    friday = 72
    saturday = 26

    # Calculate the total temperature for the week
    total_temperature = sunday + monday + tuesday + wednesday + thursday + friday + saturday

    # Calculate the average temperature for the week
    average_temperature = total_temperature / 7

    # return the result
    result = average_temperature
    return result

print(solution())