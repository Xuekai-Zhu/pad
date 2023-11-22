def solution():
    
    # Define the starting temperature and the temperature ratios
    starting_temp = 2
    low_to_high_ratio = 3
    high_to_low_ratio = 3
    high_to_high_ratio = 3
    low_time = 3
    high_time = 4
    high_time = 2

    # Calculate the temperature using the first two scenarios
    temp_1 = low_to_low_ratio * low_time
    temp_2 = high_to_high_ratio * high_time
    temp_3 = 2
    temp_4 = 2
    temp_5 = 2

    # Calculate the final temperature
    final_temp = temp_1 + temp_2 + temp_3 + temp_4 + temp_5

    # Calculate the difference between the starting temperature and the final temperature
    difference = final_temp - starting_temp

    # Display the difference in temperature
    result = difference
    return result

print(solution())