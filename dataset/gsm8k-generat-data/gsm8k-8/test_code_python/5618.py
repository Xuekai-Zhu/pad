def solution():
    # Define the hours slept each night
    monday = 8
    tuesday = 7
    wednesday = 8
    thursday = 10
    friday = 7

    # Calculate the total hours slept
    total_hours_slept = monday + tuesday + wednesday + thursday + friday

    # Calculate the average hours slept
    average_hours_slept = total_hours_slept / 5
    result = average_hours_slept
    return result

print(solution())