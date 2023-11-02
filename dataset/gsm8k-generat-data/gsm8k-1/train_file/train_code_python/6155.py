def solution():
    """A man drives 60 mph for 3 hours. How fast would he have to drive over the next 2 hours to get an average speed of 70 mph?"""
    distance1 = 60 * 3
    total_distance = distance1 + (x * 2)
    average_speed = 70
    x = (average_speed * 5) - distance1
    speed_needed = x / 2
    result = speed_needed
    return result

print(solution())