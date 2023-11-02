def solution():
    """Two friends are racing three miles. The first one runs it in 21 minutes. The second one runs it in 24 minutes. If they keep up the same pace, how long combined will it take for them to run 5 miles each?"""
    # Define the distance and time taken by each friend to run 3 miles
    distance = 3
    time_1 = 21
    time_2 = 24

    # Calculate their respective speeds
    speed_1 = distance / time_1
    speed_2 = distance / time_2

    # Calculate the time taken by each friend to run 5 miles using their speed
    time_5_miles_1 = 5 / speed_1
    time_5_miles_2 = 5 / speed_2

    # Calculate the total time taken for both friends to run 5 miles each
    total_time = time_5_miles_1 + time_5_miles_2

    # Return the result
    result = round(total_time)
    return result

print(solution())