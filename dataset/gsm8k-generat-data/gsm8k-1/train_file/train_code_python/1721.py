def solution():
    """In a car racing competition, Skye drove a 6-kilometer track. For the first 3 kilometers, his speed was 150 kilometers per hour. For the next 2 kilometers, his speed was 50 kilometers per hour more. For the remaining 1 kilometer, his speed was twice as fast as his speed on the first 3 kilometers. What is Skye's average speed for the entire race?"""
    distance1 = 3
    speed1 = 150
    distance2 = 2
    speed2 = speed1 + 50
    distance3 = 1
    speed3 = speed1 * 2
    total_distance = distance1 + distance2 + distance3
    total_time = (distance1 / speed1) + (distance2 / speed2) + (distance3 / speed3)
    average_speed = total_distance / total_time
    result = average_speed
    return result

print(solution())