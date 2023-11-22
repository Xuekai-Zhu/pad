def solution():
    
    # Define the initial temperature and the time spent baking
    initial_temp = 40
    time_baking = 3

    # Calculate the temperature increase due to baking
    temp_increase = time_baking * 5

    # Calculate the temperature increase due to the window open
    temp_increase = temp_increase * 10

    # Calculate the final temperature
    final_temp = initial_temp + temp_increase - temp_increase

    # Display the final temperature
    result = final_temp
    return result

print(solution())