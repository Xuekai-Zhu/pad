def solution():
    
    # Define the number of days Brian ran the dehumidifier
    days = 3

    # Define the number of water removed per day for each setting
    low_setting = 1
    medium_setting = 2 * low_setting
    high_setting = 2 * medium_setting

    # Calculate the total water removed in 3 days
    total_water_removed = low_setting + medium_setting + high_setting

    # Calculate the total water removed in 3 days
    total_water_removed += total_water_removed * days

    # Display the total water removed in 3 days
    result = total_water_removed
    return result

print(solution())