def solution():
    """In a car racing competition, Skye drove a 6-kilometer track. For the first 3 kilometers, his speed was 150 kilometers per hour. For the next 2 kilometers, his speed was 50 kilometers per hour more. For the remaining 1 kilometer, his speed was twice as fast as his speed on the first 3 kilometers. What is Skye's average speed for the entire race?"""
    # Calculate the time taken for Skye to cover the first 3 kilometers
    time1 = 3 / 150

    # Calculate Skye's speed for the next 2 kilometers
    speed2 = 150 + 50

    # Calculate the time taken for Skye to cover the next 2 kilometers
    time2 = 2 / speed2

    # Calculate Skye's speed for the remaining 1 kilometer
    speed3 = 150 * 2

    # Calculate the time taken for Skye to cover the remaining 1 kilometer
    time3 = 1 / speed3

    # Calculate the total time taken for Skye to complete the race
    total_time = time1 + time2 + time3

    # Calculate Skye's average speed for the entire race
    average_speed = 6 / total_time

    # Display Skye's average speed for the entire race
    result = average_speed
    return result

print(solution())