def solution():
    """In a car racing competition, Skye drove a 6-kilometer track. For the first 3 kilometers, his speed was 150 kilometers per hour. For the next 2 kilometers, his speed was 50 kilometers per hour more. For the remaining 1 kilometer, his speed was twice as fast as his speed on the first 3 kilometers. What is Skye's average speed for the entire race?"""
    # Define the distances and speeds for each segment
    distance1 = 3
    speed1 = 150

    distance2 = 2
    speed2 = 200

    distance3 = 1
    speed3 = 300

    # Calculate the total time taken to complete the race
    time = distance1 / speed1 + distance2 / speed2 + distance3 / speed3

    # Calculate the average speed for the entire race
    average_speed = 6 / time

    result = round(average_speed)
    return result

print(solution())