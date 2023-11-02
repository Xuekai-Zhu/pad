def solution():
    """Emery's family decides to travel for a weekend trip. They drive the first 100 miles in 1 hour. They stop at a McDonald's and then continue the rest of the journey for 300 miles. What's the total number of hours they traveled?"""
    # Define the distance covered and the time taken for the first part of the journey
    distance_1 = 100
    time_1 = 1

    # Define the distance for the second part of the journey
    distance_2 = 300

    # Define the average speed for the first part of the journey
    speed_1 = distance_1 / time_1

    # Calculate the time taken for the second part of the journey
    time_2 = distance_2 / speed_1

    # Calculate the total time taken
    total_time = time_1 + time_2

    result = total_time
    return result

print(solution())