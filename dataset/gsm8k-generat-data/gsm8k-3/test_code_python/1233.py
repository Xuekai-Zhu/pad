def solution():
    """Kevin has been for a run and wants to calculate how far he traveled. He ran at 10 miles per hour for half an hour,
    20 miles per hour for half an hour, then ran at 8 miles per hour for 15 minutes. How many miles has Kevin run?"""
    # Define the speed and time of each portion of the run
    SPEED_1 = 10
    SPEED_2 = 20
    SPEED_3 = 8
    TIME_1 = 0.5
    TIME_2 = 0.5
    TIME_3 = 0.25

    # Calculate the distance traveled in each portion of the run
    distance_1 = SPEED_1 * TIME_1
    distance_2 = SPEED_2 * TIME_2
    distance_3 = SPEED_3 * TIME_3

    # Calculate the total distance traveled
    total_distance = distance_1 + distance_2 + distance_3

    # Display the total distance traveled
    result = total_distance
    return result

print(solution())