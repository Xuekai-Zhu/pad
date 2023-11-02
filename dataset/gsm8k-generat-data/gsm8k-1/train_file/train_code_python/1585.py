def solution():
    """Emma traveled by car 280 miles in 2 hours 20 minutes. What was the average speed of the car in miles per hour?"""
    distance = 280
    time_in_hours = 2 + (20/60)
    speed = distance / time_in_hours
    result = speed
    return result

print(solution())