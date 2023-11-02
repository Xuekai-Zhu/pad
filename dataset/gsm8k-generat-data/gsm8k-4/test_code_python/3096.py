def solution():
    """Two days ago, the temperature in the morning went up 1.5 degrees every 2 hours. If the temperature was 50 degrees at 3 A.M., what was the temperature at 11 A.M.?"""
    # Define the initial temperature and the time elapsed
    initial_temp = 50
    time_elapsed = 8

    # Calculate the temperature increase per hour
    temp_increase_per_hour = 1.5 / 2

    # Calculate the final temperature using the formula: final temp = initial temp + (temp increase per hour * time elapsed)
    final_temp = initial_temp + (temp_increase_per_hour * time_elapsed)

    # return the result
    result = final_temp
    return result

print(solution())