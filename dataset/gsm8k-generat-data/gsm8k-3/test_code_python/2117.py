def solution():
    """Two friends are racing three miles. The first one runs it in 21 minutes. The second one runs it in 24 minutes. If they keep up the same pace, how long combined will it take for them to run 5 miles each?"""
    # Define the distance and time for the first friend
    distance_1 = 3
    time_1 = 21

    # Define the distance and time for the second friend
    distance_2 = 3
    time_2 = 24

    # Calculate the speed of each friend
    speed_1 = distance_1 / (time_1 / 60)  # in miles per hour
    speed_2 = distance_2 / (time_2 / 60)  # in miles per hour

    # Calculate the time it takes for each friend to run 5 miles
    time_5_1 = (5 / speed_1) * 60  # in minutes
    time_5_2 = (5 / speed_2) * 60  # in minutes

    # Calculate the total time it takes for them to run 5 miles each
    total_time = time_5_1 + time_5_2

    # Display the total time
    result = total_time
    return result

print(solution())