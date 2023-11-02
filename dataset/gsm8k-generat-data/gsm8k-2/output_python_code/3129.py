def solution():
    """Jace drives 60 miles per hour. If Jace drives for 4 hours straight, take a 30-minute break, and then drives for another 9 hours straight, how many miles will he travel?"""
    driving_speed = 60
    driving_time_1 = 4
    driving_time_2 = 9
    break_time = 0.5 # in hours
    total_driving_time = driving_time_1 + driving_time_2 + break_time
    distance = total_driving_time * driving_speed
    result = distance
    return result

print(solution())