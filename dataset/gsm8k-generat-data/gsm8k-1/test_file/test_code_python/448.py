def solution():
    """A car is on a road trip and drives 60 mph for 2 hours, and then 30 mph for 1 hour. What is the car's average speed in mph during this trip?"""
    distance_first_leg = 60 * 2
    distance_second_leg = 30 * 1
    total_distance = distance_first_leg + distance_second_leg
    total_time = 2 + 1
    average_speed = total_distance / total_time
    result = average_speed
    return result

print(solution())