def solution():
    """It starts raining at 7:00 and pours heavily until its stops at 17:00  on a particular day. On the second day, the rain takes 2 more hours than it took on the first day to stop. On the third day, the rain pours for twice the amount of time it took on the second day. Calculate the total time it was raining in the three days."""
    # Define the number of hours it rained on the first day
    day_1 = 10

    # Define the number of hours it rained on the second day
    day_2 = day_1 + 2

    # Define the number of hours it rained on the third day
    day_3 = day_2 * 2

    # Calculate the total number of hours it rained
    total_rain_time = day_1 + day_2 + day_3

    # Display the total rain time
    result = total_rain_time
    return result

print(solution())