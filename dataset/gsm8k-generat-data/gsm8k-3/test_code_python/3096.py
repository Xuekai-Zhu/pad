def solution():
    """Two days ago, the temperature in the morning went up 1.5 degrees every 2 hours. If the temperature was 50 degrees at 3 A.M., what was the temperature at 11 A.M.?"""
    # Define the starting temperature and the temperature increase per hour
    start_temp = 50
    increase_per_hour = 1.5 / 2

    # Calculate the number of hours between 3 A.M. and 11 A.M.
    hours_passed = 8

    # Calculate the temperature increase during this time
    temp_increase = hours_passed * increase_per_hour

    # Calculate the final temperature at 11 A.M.
    final_temp = start_temp + temp_increase

    # Display the final temperature
    result = final_temp
    return result

print(solution())