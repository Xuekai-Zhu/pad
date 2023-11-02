def solution():
    """Emma traveled by car 280 miles in 2 hours 20 minutes. What was the average speed of the car in miles per hour?"""
    total_hours = 2 + (20/60)  # Convert 20 minutes to hours
    distance = 280
    average_speed = distance / total_hours
    result = average_speed
    return result

print(solution())