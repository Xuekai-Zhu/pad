def solution():
    """September's temperature fluctuated severely in 1 week.  They started off with 40 degrees on Sunday then hit 50 on Monday, 65 on Tuesday, 36 on Wednesday, 82 on Thursday, 72 on Friday and ended the week at 26 on Saturday.  What was the average temperature for that week?"""
    # Define the temperatures for each day
    sunday_temp = 40
    monday_temp = 50
    tuesday_temp = 65
    wednesday_temp = 36
    thursday_temp = 82
    friday_temp = 72
    saturday_temp = 26

    # Calculate the total temperature for the week
    total_temp = sunday_temp + monday_temp + tuesday_temp + wednesday_temp + thursday_temp + friday_temp + saturday_temp

    # Calculate the average temperature for the week
    average_temp = total_temp / 7

    # Display the average temperature
    result = average_temp
    return result

print(solution())