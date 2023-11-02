def solution():
    """Kevin has been for a run and wants to calculate how far he traveled. He ran at 10 miles per hour for half an hour, 20 miles per hour for half an hour, then ran at 8 miles per hour for 15 minutes. How many miles has Kevin run?"""
    # Define the distances traveled at each speed
    distance_1 = 10 * 0.5
    distance_2 = 20 * 0.5
    distance_3 = 8 * (15/60)

    # Calculate the total distance traveled
    total_distance = distance_1 + distance_2 + distance_3

    # Return the total distance
    result = total_distance
    return result

print(solution())